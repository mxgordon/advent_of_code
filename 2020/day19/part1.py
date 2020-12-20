import numpy as np
import math


with open("data.txt", 'r') as f:
    first, second = f.read().split("\n\n")
    first, second = first.split("\n"), second.split("\n")

rules = {int(line.split(": ")[0]): line.split(": ")[1] for line in first}

for n in rules:
    rule = rules[n]
    if rule.count("|") > 0:
        rule = list(map(lambda x: tuple(map(int, x.split())), rule.split(" | ")))
    elif rule.count('"') > 0:
        rule = rule.strip('"')
    else:
        rule = tuple(map(int, rule.split()))
        rule = rule if len(rule) > 1 else rule[0]
    rules[n] = rule


def L(thing):
    if not isinstance(thing, list):
        thing = [thing]
    return thing


def correct(f, s):
    if isinstance(f, str) and isinstance(s, str):
        return f + s
    else:
        return list(f) + list(s)


def tup(f, s):
    if isinstance(f, str) and isinstance(s, str):
        return f + s
    elif isinstance(f, list) and isinstance(s, list):
        new = []
        for fst in f:
            new += list(map(lambda x: fst + x, s))
        return new
    elif isinstance(f, list) and isinstance(s, str):
        return [e + s for e in f]
    elif isinstance(f, str) and isinstance(s, list):
        return [f + e for e in s]
    else:
        raise RuntimeError()


def lst(f, s):
    if isinstance(f, str):
        f = [f]
    if isinstance(s, str):
        s = [s]
    return s + f


def idk(ele):
    if len(ele) == 1:
        return get_letter_list(ele[0])
    else:
        return tup(*map(get_letter_list, ele))


def get_letter_list(key):
    rule = rules[key]

    if isinstance(rule, str):
        return rule
    elif isinstance(rule, int):
        return get_letter_list(rule)
    elif isinstance(rule, tuple):
        return tup(get_letter_list(rule[0]), get_letter_list(rule[1]))
    elif isinstance(rule, list):
        first = idk(rule[0])
        second = idk(rule[1])
        return lst(first, second)
    else:
        raise RuntimeError()


all_rules = {*get_letter_list(0)}
num = 0
for pic in second:
    if pic in all_rules:
        num += 1

print(num)

