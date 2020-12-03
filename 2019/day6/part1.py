import json


with open('data.json', 'r') as f:
    raw = json.load(f)

raw_split = [(raw_peice.split(')')[0], raw_peice.split(')')[1]) for raw_peice in raw]

all = {'COM': (0, None)}

count = 0


while count < len(raw_split):
    for num, orbits in enumerate(raw_split):
        orbitee, orbiter = orbits
        if all.get(orbitee) is not None:
            all.update({orbiter: (all[orbitee][0] + 1, orbitee)})
            count += 1
            raw_split[num] = (None, None)
        # print(orbitee == 'COM')
    if count % 10 == 0:
        print(count, len(raw_split))

print(len(all))
total = 0
print(sum([A[0] for A in all.values()]))