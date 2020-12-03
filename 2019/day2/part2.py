# import numpy as np
import json


with open('intcode.json', 'r') as f:
    intcodes = json.load(f)

with open('intcode.json', 'r') as f:
    safe = json.load(f)

assert safe == intcodes

for first in range(100):
    # print(f"****{first}")
    for second in range(100):
        # print(f"-----{second}")
        with open('intcode.json', 'r') as f:
            intcodes = json.load(f)
        # intcodes = safe
        assert safe == intcodes
        intcodes[1] = first
        intcodes[2] = second
        try:
            for index in range(len(intcodes) // 4):
                index = index * 4
                # print(index)
                opcode = intcodes[index]
                pos1 = intcodes[index + 1]
                pos2 = intcodes[index + 2]
                store_pos = intcodes[index + 3]

                if opcode == 1:
                    intcodes[store_pos] = intcodes[pos1] + intcodes[pos2]

                elif opcode == 2:
                    intcodes[store_pos] = intcodes[pos1] * intcodes[pos2]

                elif opcode == 99:
                    # print(intcodes[0])
                    # raise SystemExit(f"Got 99 at index {index}")
                    break

                else:
                    raise ValueError(f"Got opcode {opcode} at position {index}")
        except SystemExit and ValueError:
            pass

        if intcodes[0] == 19690720:
            print(first, second)
