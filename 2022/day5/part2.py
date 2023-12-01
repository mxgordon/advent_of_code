with open("data.txt", 'r') as f:
    data = f.read()
    crate_data, data = data.split("\n\n")

crate_data = crate_data.split("\n")[:-1]
crates = []

data = [(int(d.split(" ")[1]), int(d.split(" ")[3]), int(d.split(" ")[5])) for d in data.split("\n")]

for line in crate_data:
    crates.append([line[i+1] for i in range(0, len(line), 4)])

crate_stack = [[] for _ in crates[0]]

for i in range(len(crates[0])):
    for j in range(len(crates))[::-1]:
        if crates[j][i] != " ":
            crate_stack[i].append(crates[j][i])

for count, from_, to in data:
    crate_stack[to - 1] += crate_stack[from_ - 1][-count:]
    del crate_stack[from_ - 1][-count:]

print("".join(([c.pop() for c in crate_stack])))
