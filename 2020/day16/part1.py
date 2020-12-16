with open("data.txt", 'r') as f:
    rules, mine, others = [r.split('\n') for r in f.read().split('\n\n')]

allns = set()
for rule in rules:
    nums = [[int(n) for n in rang.split("-")] for rang in rule.split(":")[1][1:].split(" or ")]
    ns = set(range(nums[0][0], nums[0][1]+1)).union(set(range(nums[1][0], nums[1][1]+1)))
    allns = allns.union(ns)

otherts = []
for ticket in others[1:]:
    otherts += list(map(int, ticket.split(',')))

error = 0
for o in otherts:
    if o not in allns:
        error+= o

print(error)
