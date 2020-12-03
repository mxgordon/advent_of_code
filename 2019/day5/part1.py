import json
from typing import Tuple, List


def parse_instruction(instruction_block: int) -> Tuple[int, List[int]]:
    params = [int(num) for num in str(instruction_block)[:-2]][::-1]
    opcode = int(str(instruction_block)[-2:])

    while len(params) < 3:
        params.append(0)
    print(opcode)

    assert opcode in [1, 2, 3, 4, 99]
    assert params[-1] == 0
    assert len(params) == 3
    return opcode, params


def get_values(params: List[int], index: int, intcode: List[int]):
    block = intcode[index:index + len(params) - 1]
    values = []

    for param, data in tuple(zip(params[0:2], block)):
        if param == 0:
            values.append(intcode[data])
        if params == 1:
            values.append(data)
    return values


def add(*nums: int) -> int:
    num = 0
    for i in nums:
        num += i
    return num


def multiply(*nums: int) -> int:
    num = 0
    for i in nums:
        num *= i
    return num


if __name__ == '__main__':
    with open("intcode.json", 'r') as f:
        intcode = json.load(f)

    index = 0
    while index < len(intcode):
        opcode, params = parse_instruction(intcode[index])
        if opcode == 1:
            values = get_values(params, index, intcode)
            intcode[index + 3] = add(*values)
            index += 4

        elif opcode == 2:
            values = get_values(params, index, intcode)
            intcode[index + 3] = multiply(*values)
            index += 4

        elif opcode == 3:
            intcode[intcode[index + 1]] = int(input("Need int: "))
            index += 2

        elif opcode == 3:
            print(intcode[intcode[index + 1]])
            index += 2

        elif index == 99:
            print("---- EOF ----")
            break

        else:
            raise ValueError(f"Unknown opcode {opcode} at {index}")


