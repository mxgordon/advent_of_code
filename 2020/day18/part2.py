import re


with open("data.txt", 'r') as f:
    data = f.read().strip().split('\n')


def solve(exp: list):

    while list(filter(lambda x: x == "+", exp)):
        i = exp.index("+")
        exp[i-1] = int(exp[i-1]) + int(exp[i+1])
        del exp[i:i+2]

    num = int(exp[0])
    for thing in exp[1:]:
        if thing != "*":
            num = num * int(thing)
    return num


def solve_top_parans(equ):
    front, back = 0, 0
    ptn = r"\(.*\)"
    if re.findall(ptn, equ):
        for i in range(len(equ)):
            if not re.findall(ptn, equ[i:]):
                for j in range(1, len(equ)):
                    if not re.findall(ptn, equ[i - 1:-j]):
                        front, back = i - 1, -(j - 1)
                        break
                break
        equ = f"{equ[:front]}{solve(equ[front + 1:back - 1].split())}{equ[back:] if back != 0 else ''}"
    else:
        return solve(equ.split())

    return solve_top_parans(equ)


s = 0
for d in data:
    s += solve_top_parans(d)
print(s)

