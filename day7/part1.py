import json
from typing import Tuple, List
import math


class BigReturn(Exception):
    pass


class SmallReturn(Exception):
    pass


def parse_instruction(instruction_block: int) -> Tuple[int, List[int]]:
    params = [int(num) for num in str(instruction_block)[:-2]][::-1]
    opcode = int(str(instruction_block)[-2:])

    while len(params) < 3:
        params.append(0)

    # assert opcode in [1, 2, 3, 4, 99]
    assert params[-1] == 0
    assert len(params) == 3
    return opcode, params


def get_values(params: List[int], index: int, intcode: List[int]):
    block = intcode[index +1:index + len(params)]
    values = []

    for param, data in tuple(zip(params[0:2], block)):
        if param == 0:
            values.append(intcode[data])
        elif param == 1:
            values.append(data)
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


def gen_num_list():
    final = []
    for i in range(5, 10):
        for j in [j for j in range(5, 10) if j not in [i]]:
            for k in [k for k in range(5, 10) if k not in [i, j]]:
                for n in [n for n in range(5, 10) if n not in [i, j, k]]:
                    for m in [m for m in range(5, 10) if m not in [i, j, k, n]]:
                        final.append([i, j, k, n, m])
    print(len(final), math.factorial(6))
    assert len(final) == math.factorial(5)
    return [[9, 8, 7, 6, 5]]


if __name__ == '__main__':
    with open("data.json", 'r') as f:
        intcode = json.load(f)

    amp_list = gen_num_list()

    finals = []
    for input_set in amp_list:
        print(input_set)
        try:
            carry = 0
            while True:
                for input_amp in input_set:
                    print(f"**{carry}")
                    first = True
                    index = 0
                    carry_tmp = 0
                    while index < len(intcode):
                        opcode, params = parse_instruction(intcode[index])
                        if opcode == 1:  # add
                            values = get_values(params, index, intcode)
                            intcode[intcode[index + 3]] = add(*values)
                            index += 4

                        elif opcode == 2:  # multiply
                            values = get_values(params, index, intcode)
                            intcode[intcode[index + 3]] = multiply(*values)
                            index += 4

                        elif opcode == 3:  # input
                            print(f"getting input... {first}")
                            if first:
                                intcode[intcode[index + 1]] = input_amp
                                first = False
                            else:
                                intcode[intcode[index + 1]] = carry_tmp
                            index += 2

                        elif opcode == 4:  # output
                            print(intcode[intcode[index + 1]])
                            carry_tmp = intcode[intcode[index + 1]]
                            index += 2

                        elif opcode == 5:  # jump if true
                            values = get_values(params, index, intcode)
                            if values[0] != 0:
                                index = values[1]
                            else:
                                index += 3

                        elif opcode == 6:  # jump if false
                            values = get_values(params, index, intcode)
                            if values[0] == 0:
                                index = values[1]
                            else:
                                index += 3

                        elif opcode == 7:  # less than
                            values = get_values(params, index, intcode)
                            if values[0] < values[1]:
                                intcode[intcode[index + 3]] = 1
                            else:
                                intcode[intcode[index + 3]] = 0
                            index += 4

                        elif opcode == 8:  # equals
                            values = get_values(params, index, intcode)
                            if values[0] == values[1]:
                                intcode[intcode[index + 3]] = 1
                            else:
                                intcode[intcode[index + 3]] = 0
                            index += 4

                        elif opcode == 99:  # end
                            print("---- EOF ----")
                            raise BigReturn
                            # break

                        else:
                            raise ValueError(f"Unknown opcode {opcode} at {index}")
        except BigReturn:
            pass

        finals.append(carry)

    print('\n---------------------\n')
    print(max(finals))
