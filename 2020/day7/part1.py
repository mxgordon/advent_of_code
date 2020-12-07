import json


with open("data.json", 'r') as f:
    data = json.load(f)


def get_bags(base):
    bgs = set()
    for bag, outs in data:
        outs = [*map(lambda x: x[1], outs)]
        if base in outs:
            bgs = bgs.union({bag, *get_bags(bag)})
    return bgs


print(len(get_bags("shiny gold")))
