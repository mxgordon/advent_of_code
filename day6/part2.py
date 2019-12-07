import json


with open('data.json', 'r') as f:
    raw = json.load(f)

raw_split = [(raw_peice.split(')')[0], raw_peice.split(')')[1]) for raw_peice in raw]

all = {'COM': (0, None)}

count = 0


def go_till_com(dictionary, find, x=0):
    total = []
    tmp = []
    if dictionary[find][1] != "COM":
        total.append(dictionary[find][1])
        x += 1
        x, tmp = go_till_com(dictionary, dictionary[find][1], x=x)
    total = [*total, *tmp]
    return x, total


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

x, you = go_till_com(all, 'YOU')
y, san = go_till_com(all, 'SAN')

you = you[::-1]
san = san[::-1]

for i in range(max(len(you), len(san))):
    if you[i] != san[i]:
        print(len(you[i:]))
        print(you[i:])
        print(len(san[i:]))
        print(san[:i])
        pass