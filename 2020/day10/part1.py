with open("data.txt", 'r') as f:
    data = [int(line) for line in f.readlines()]

data.sort()
data = [0]+data
ones = 0
threes = 1

for i, j in zip(data[:-1], data[1:]):
    if j-i == 1:
        ones += 1
    elif j-i == 3:
        threes += 1

print(threes * ones)
