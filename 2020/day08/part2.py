import json


with open("data.json", 'r') as f:
    data = json.load(f)


def run_code(code):
    lines = []
    current_line = 0
    accumulator = 0
    try:
        while current_line not in lines:
            lines.append(current_line)
            inst, n = code[current_line]
            if inst == "acc":
                accumulator += n
                current_line += 1
            elif inst == "jmp":
                current_line += n
            elif inst == "nop":
                current_line += 1
            else:
                raise RuntimeError
        return accumulator, False
    except IndexError:
        return accumulator, True


acc, goodly = run_code(data)

times = 1
for i, line in enumerate(data):
    inst, _ = line
    if inst == "acc":
        continue
    times += 1

    data[i][0] = 'nop' if inst == 'jmp' else 'jmp'

    acc, goodly = run_code(data)
    if goodly:
        print(acc)
        break
    else:
        data[i][0] = inst