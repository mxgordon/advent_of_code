import json

with open('intcode.json', 'r') as f:
    intcodes = json.load(f)

intcodes[1] = 12
intcodes[2] = 2



for index in range(len(intcodes)//4):
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
        print(intcodes[0])
        raise SystemExit(f"Got 99 at index {index}")

    else:
        raise ValueError(f"Got opcode {opcode} at position {index}")

print(intcodes[0])


