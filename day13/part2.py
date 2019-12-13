import json
from typing import Tuple, List
import os
from time import sleep

import keyboard
import numpy as np


class Store:
    def __init__(self):
        self.x = None
        self.y = None
        self.tile_id = None
        self.full = False
        self.saves = []

    def put(self, num, index):
        if self.x is None:
            self.x = num
            self.x_index = index
        elif self.y is None:
            self.y = num
            self.y_index = index
        elif self.tile_id is None:
            # assert 0 <= num <= 4
            self.tile_id = num
            self.full = True

        if num == 4 and self.tile_id is not None:
            self.saves.append((self.x_index, self.y_index))

    def dump(self):
        assert self.full
        x, y, tile_id = self.x, self.y, self.tile_id
        self.x, self.y, self.tile_id, self.full = None, None, None, False
        self.x_index, self.y_index = None, None
        return x, y, tile_id


class Board:
    def __init__(self, x=42, y=25):
        self.board = np.ndarray((x, y), dtype=int)
        self.board.fill(-1)
        self.final = None
        self.score = 0

    def draw(self, x, y, id):
        if x == -1:
            self.score = id
        else:
            self.board[x, y] = id

    def print(self):
        self.final = '\n'.join([str(str_line).replace(',', '').replace(' ', '').replace('-1', 'X').replace('\n', '') for str_line in np.rot90(self.board)])
        self.final = self.final.replace('0', '.').replace('1', '▏').replace('2', '▆').replace('3', '_'). replace('4', 'O')
        os.system('clear')
        print(self.final)
        print(f"Score: {self.score}")

    def count(self):
        return np.sum(self.board == 2)



def write(intcode: List[int], value: int, param: int, index: int, base: int):
    if param == 0:
        intcode[intcode[index]] = value
    elif param == 2:
        intcode[intcode[index] + base] = value
    else:
        raise ValueError(f"Got param {param}")
    return intcode


def parse_instruction(instruction_block: int) -> Tuple[int, List[int]]:
    params = [int(num) for num in str(instruction_block)[:-2]][::-1]
    opcode = int(str(instruction_block)[-2:])

    while len(params) < 3:
        params.append(0)

    # assert opcode in [1, 2, 3, 4, 99]
    assert params[-1] in [0, 2]
    assert len(params) == 3
    return opcode, params


def get_values(params: List[int], index: int, intcode: List[int], base: int):
    block = intcode[index + 1:index + len(params)]
    values = []

    for param, data in tuple(zip(params[0:2], block)):
        if param == 0:
            values.append(intcode[data])
        elif param == 1:
            values.append(data)
        elif param == 2:
            values.append(intcode[data + base])
    assert len(values) == 2
    return values


def add(*nums: int) -> int:
    num = 0
    for i in nums:
        num += i
    return num


def multiply(*nums: int) -> int:
    num = 1
    for i in nums:
        num *= i
    return num


def get_key():

    print("Input: ", end='')
    while True:
        a = keyboard.read_key()
        if a in ['a', 's', 'd']:
            sleep(0.12)
            return a.replace('a', '-19191919').replace('s', '0').replace('d', '19191919')


if __name__ == '__main__':
    with open("data.json", 'r') as f:
        intcode = json.load(f)

    for i in range(1000000):
        intcode.append(0)

    storage = Store()
    board = Board()
    coords = []

    base = 0

    index = 0
    while index < len(intcode):

        if storage.full:
            hide = storage.saves
            a = storage.dump()
            board.draw(*a)
            board.print()
            # print(intcode.index(a[0]))
            # print(intcode.index(a[1]))
            # print("Last write: ", a[2])
            # print("Coords: ", hide)
            # coords.append(storage.dump()[0:2])

        opcode, params = parse_instruction(intcode[index])
        values = get_values(params, index, intcode, base)

        if opcode == 1:  # add

            intcode = write(intcode, add(*values), params[2], index + 3, base)
            index += 4

        elif opcode == 2:

            intcode = write(intcode, multiply(*values), params[2], index + 3, base)
            index += 4

        elif opcode == 3:  # input
            # intcode[389] = 1
            # print("====", index +1)
            intcode = write(intcode, int(get_key()), params[0], index + 1, base)
            # intcode[568] = 10
            # intcode[570] = 20
            index += 2

        elif opcode == 4:  # output
            # print(values[0])
            # print("**", values[0])
            storage.put(values[0], index + 1)
            index += 2

        elif opcode == 5:  # jump if true
            if values[0] != 0:
                index = values[1]
            else:
                index += 3

        elif opcode == 6:  # jump if false
            if values[0] == 0:
                index = values[1]
            else:
                index += 3

        elif opcode == 7:  # less than
            # if 19191919 in [values[0], values[1]]:
            #     intcode = write(intcode, 2, params[2], index + 3, base)
            # print([values[0], values[1]])
            # print([intcode[index + 1], intcode[index + 2]])
            if -19191919 in [values[0], values[1]]:
                intcode = write(intcode, -2, params[2], index + 3, base)
            else:
                intcode = write(intcode, 1 if values[0] < values[1] else 0, params[2], index + 3, base)
            index += 4

        elif opcode == 8:  # equals
            intcode = write(intcode, 1 if values[0] == values[1] else 0, params[2], index + 3, base)
            index += 4

        elif opcode == 9:
            base += values[0]
            index += 2

        elif opcode == 99:  # end
            print("---- EOF ----")
            break

        else:
            raise ValueError(f"Unknown opcode {opcode} at {index}")
    board.print()
    print(board.count())
