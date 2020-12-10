import json


with open("data.json", 'r') as f:
    data = json.load(f)


def get_bags(base, b=False):
    ots = None
    for bag, outs in data:
        if bag == base:
            ots = outs

    if ots == [(1, 'no other')]:
        return 1

    num = 0
    for n, out in ots:
        for bag, outs in data:
            if out == bag:
                num += n * get_bags(bag)
    return num + (1 if not b else 0)


print(get_bags("shiny gold", True))
