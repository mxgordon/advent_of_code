import json
from typing import Tuple, List


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


if __name__ == '__main__':
    with open("data.json", 'r') as f:
        intcode = json.load(f)

    for i in range(1000000):
        intcode.append(0)

    base = 0

    index = 0
    while index < len(intcode):
        opcode, params = parse_instruction(intcode[index])
        values = get_values(params, index, intcode, base)

        if opcode == 1:  # add

            intcode = write(intcode, add(*values), params[2], index + 3, base)
            index += 4

        elif opcode == 2:

            intcode = write(intcode, multiply(*values), params[2], index + 3, base)
            index += 4

        elif opcode == 3:  # input
            intcode = write(intcode, int(input("Need int: ")), params[0], index + 1, base)
            index += 2

        elif opcode == 4:  # output
            print(values[0])
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
