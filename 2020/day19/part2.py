import numpy as np
import math


with open("data.txt", 'r') as f:
    first, second = f.read().split("\n\n")
    first, second = first.split("\n"), second.split("\n")

rules = {int(line.split(": ")[0]): [[int(n) for n in ns.split()] for ns in line.split(": ")[1].split(" | ")] if line.split(": ")[1][0] != '"' else line.split(": ")[1][1] for line in first}


def check_pic(pic, rule):
    if isinstance(rules[rule], str):
        if pic and pic[0] == rules[rule]:
            return [pic[1:]]

    else:
        a = []  # TODO idk what this is
        for rule_set in rules[rule]:
            vrs = [pic]
            for rl in rule_set:
                vrs2 = []
                for vr in vrs:
                    vrs2 += check_pic(vr, rl)

                vrs = vrs2
                if not vrs:
                    break
            if vrs:
                a += vrs
        return a
    return []


rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

print(sum('' in check_pic(msg, 0) for msg in second))
