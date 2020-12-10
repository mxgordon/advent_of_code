import json


with open("data.json", 'r') as f:
    data = json.load(f)

lines = []
current_line = 0
accumulator = 0
while current_line not in lines:
    lines.append(current_line)
    inst, n = data[current_line]
    if inst == "acc":
        accumulator += n
        current_line += 1
    elif inst == "jmp":
        current_line += n
    elif inst == "nop":
        current_line += 1
    else:
        raise RuntimeError

print(accumulator)
