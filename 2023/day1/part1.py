with open("data.txt", 'r') as f:
    data = f.readlines()

nums = [[*filter(str.isnumeric, d)] for d in data]
nums = [int("".join((n[0], n[-1],))) for n in nums]

print(sum(nums))
