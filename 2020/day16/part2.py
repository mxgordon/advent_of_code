import numpy as np

# This could prolly be cleaned up a bunch but I don't really care
with open("data.txt", 'r') as f:
    rules, mine, others = [r.split('\n') for r in f.read().split('\n\n')]

allns = set()
splits = {}
for rule in rules:
    nums = [[int(n) for n in rang.split("-")] for rang in rule.split(":")[1][1:].split(" or ")]
    ns = set(range(nums[0][0], nums[0][1]+1)).union(set(range(nums[1][0], nums[1][1]+1)))
    allns = allns.union(ns)

    splits[rule.split(":")[0]] = ns.copy()

otherts = []
for ticket in others[1:]:
    otherts.append(list(map(int, ticket.split(','))))

for line in otherts.copy():
    for o in line:
        if o not in allns:
            otherts.remove(line)
            break

allts = np.array(otherts)

matches = {}
good = False
for i, col in enumerate(allts.T):
    matches[i] = []
    for key in splits.keys():
        ins = [n in splits[key] for n in col]
        if all(ins):
            matches[i].append(key)

order = sorted(matches.items(), key=lambda x: len(x[1]))
used = []

mines = list(map(int, mine[1].split(',')))
nums = 1
for i, fields in order:
    fields = list(filter(lambda x: x not in used, fields))
    assert len(fields) == 1
    used += fields

    if fields[0].split()[0] == "departure":
        nums *= mines[i]

print(nums)
