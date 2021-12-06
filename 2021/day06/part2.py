with open("data.txt", 'r') as f:
    data = f.readlines()
    data = list(map(int, data[0].strip().split(",")))

fish = [data.count(i) for i in range(9)]

for i in range(256):
    num = fish.pop(0)

    fish[6] += num
    fish.append(num)

    assert len(fish) == 9

print(sum(fish))