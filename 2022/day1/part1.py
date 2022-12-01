with open("data.txt", 'r') as f:
    data = f.read()

data = [sum(map(int, d.split())) for d in data.split("\n\n")]

print(max(data))
