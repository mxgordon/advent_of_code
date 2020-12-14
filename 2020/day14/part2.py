with open("data.txt", 'r') as f:
    data = [("mask" + lines).split('\n') for lines in f.read().split('mask')][1:]

code = []

for c in data:
    code.append((c[0].split()[-1], [[int(line.split()[0][4:-1]), int(line.split()[2])] for line in c[1:-1]]))


def getalladdr(addr: str):
    addresses = []
    x = addr.find('X')
    if x != -1:
        addresses += [addr.replace('X', '1', 1), addr.replace('X', '0', 1)]
        return getalladdr(addresses[0]) + getalladdr(addresses[1])
    else:
        return [addr]


mem = {}

for mask, writes in code:
    for loc, num in writes:
        writeloc = zip(mask, f'{loc:36b}'.replace(' ', '0'))
        writeloc = "".join(map(lambda mb: mb[0] if mb[0] != '0' else mb[1], writeloc))

        for addr in getalladdr(writeloc):
            mem[int(addr, 2)] = num


print(sum(mem.values()))
