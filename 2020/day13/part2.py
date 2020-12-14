from functools import reduce


def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


with open("data.txt", 'r') as f:
    buses = [0 if not isint(line) else int(line) for line in f.readlines()[1].strip().split(',')]


indices = [i for i, bus in enumerate(buses) if bus]
diff = indices[-1] - indices[0]
prod = reduce(lambda a, b: a * b, filter(None, buses))
nums = []

for i, n in enumerate(buses):
    if n:
        nums.append((diff - i) * pow(prod // n, n - 2, n) * prod // n)

print(sum(nums) % prod - diff)
