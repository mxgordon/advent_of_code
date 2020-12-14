with open("data.txt", 'r') as f:
    data = f.readlines()
    time = int(data[0])
    data = data[1].strip().split(',')


def isint(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


data = list(map(int, filter(isint, data)))
lowest = [0, 9999999999]

for d in data:
    lowest = min([d, (time - (time % d)) + d], lowest, key=lambda x: x[1])

print(lowest[0] * (lowest[1]-time))
