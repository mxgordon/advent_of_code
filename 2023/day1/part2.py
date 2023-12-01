with open("data.txt", 'r') as f:
    data = f.readlines()

for i, line in enumerate(data):
    line = line.replace("one", "o1e")
    line = line.replace("two", "t2o")
    line = line.replace("three", "t3e")
    line = line.replace("four", "f4r")
    line = line.replace("five", "f5e")
    line = line.replace("six", "s6x")
    line = line.replace("seven", "s7n")
    line = line.replace("eight", "e8t")
    line = line.replace("nine", "n9e")
    data[i] = line

nums = [[*filter(str.isnumeric, d)] for d in data]
nums = [int("".join((n[0], n[-1],))) for n in nums]

print(sum(nums))
