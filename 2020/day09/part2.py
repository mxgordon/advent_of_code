import json


with open("data.json", 'r') as f:
    data = json.load(f)

NUM = None


def add_nums(nums):
    ns = []
    for i, n1 in enumerate(nums):
        if i < len(nums) - 1:
            for n2 in nums[i+1:]:
                ns.append(n1+n2)
    return ns


# part 1
for i, num in enumerate(data):
    if i < 25:
        continue
    if num not in add_nums(data[i-25:i]):
        NUM = num
        break


for i in range(len(data)):
    for j in range(len(data)):
        sm = sum(data[i:j])
        if sm == NUM:
            print(max(data[i:j]) + min(data[i:j]))
            quit()
        elif sm > NUM:
            break
