with open("data.txt", 'r') as f:
    data = [("mask" + lines).split('\n') for lines in f.read().split('mask')][1:]

code = []

for c in data:
    code.append((c[0].split()[-1], [[int(line.split()[0][4:-1]), int(line.split()[2])] for line in c[1:-1]]))

mem = {}

for mask, writes in code:
    for loc, num in writes:
        bi = f'{num:36b}'.replace(' ', '0')
        final = "".join(map(lambda mb: mb[0] if mb[0] != 'X' else mb[1], zip(mask, bi)))
        mem[loc] = int(final, 2)

print(sum(mem.values()))
