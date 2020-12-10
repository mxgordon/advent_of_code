import json


with open("data.json", 'r') as f:
    data = json.load(f)


def add_nums(nums):
    ns = []
    for j, n1 in enumerate(nums):
        if j < len(nums) - 1:
            for n2 in nums[j+1:]:
                ns.append(n1+n2)
    return ns


for i, num in enumerate(data):
    if i < 25:
        continue
    if num not in add_nums(data[i-25:i]):
        print(num)
        quit()
