import json
from typing import Tuple, List
import os
from time import sleep

# import keyboard
import numpy as np


class LongStore:
    def __init__(self):
        self.ball_x = None
        self.paddle_x = None

    def put(self, ball_x=None, paddle_x=None):
        if ball_x is not None:
            self.ball_x = ball_x

        else:
            self.paddle_x = paddle_x

    def get_all(self):
        ball_x, paddle_x = self.ball_x, self.paddle_x
        # self.ball_x, self.paddle_x = None, None
        return ball_x, paddle_x


class Store:
    def __init__(self):
        self.x = None
        self.y = None
        self.tile_id = None
        self.full = False
        self.big_store = LongStore()

    def put(self, num, index=None):
        if self.x is None:
            self.x = num
            # self.x_index = index
        elif self.y is None:
            self.y = num
            # self.y_index = index
        elif self.tile_id is None:
            # assert 0 <= num <= 4
            self.tile_id = num
            self.full = True

        if self.tile_id == 3:
            self.big_store.put(ball_x=self.x)

        elif self.tile_id == 4:
            self.big_store.put(paddle_x=self.x)

    def dump(self):
        assert self.full
        x, y, tile_id = self.x, self.y, self.tile_id
        self.x, self.y, self.tile_id, self.full = None, None, None, False
        self.paddle_x, self.ball_x = None, None

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
        self.final = '\n'.join([str(str_line).replace(',', '')
                               .replace(' ', '')
                               .replace('-1', '╳')
                               .replace('\n', '') for str_line in np.rot90(self.board)])

        self.final = self.final.replace('0', '.')\
            .replace('1', '▚')\
            .replace('2', '▆')\
            .replace('3', '_')\
            .replace('4', 'O')

        # os.system('clear')
        print(self.final)
        print(f"Score: {self.score}")

    def count(self):
        return np.sum(self.board == 2)


def write(intcode_: List[int], value: int, param: int, index_: int, base_: int):
    if param == 0:
        intcode_[intcode_[index_]] = value
    elif param == 2:
        intcode_[intcode_[index_] + base_] = value
    else:
        raise ValueError(f"Got param {param}")
    return intcode_


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


def get_key(ball_x, paddle_x, f):
    # f.write(f"Ball   {ball_x}\n")
    # f.write(f'Paddle {paddle_x}\n')
    # f.write("------------------\n")
    # sleep(.3)

    print("Ball   ", ball_x)
    print("Paddle ", paddle_x)
    return paddle_x - ball_x


if __name__ == '__main__':

    with open("data.json", 'r') as f:
        intcode = json.load(f)

    with open('logs.txt', 'a') as f:

        for i in range(1000000):
            intcode.append(0)

        storage = Store()
        board = Board()
        coords = []

        base = 0

        index = 0
        while index < len(intcode):

            if storage.full:
                # hide = storage.saves

                a = storage.dump()
                board.draw(*a)
                board.print()

            opcode, params = parse_instruction(intcode[index])
            values = get_values(params, index, intcode, base)

            if opcode == 1:  # add

                intcode = write(intcode, add(*values), params[2], index + 3, base)
                index += 4

            elif opcode == 2:

                intcode = write(intcode, multiply(*values), params[2], index + 3, base)
                index += 4

            elif opcode == 3:  # input

                intcode = write(intcode, int(get_key(*storage.big_store.get_all(), f)), params[0], index + 1, base)
                index += 2

            elif opcode == 4:  # output
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
