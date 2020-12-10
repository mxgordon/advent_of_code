import numpy as np


with open("data.txt", 'r') as f:
    data = [int(line) for line in f.readlines()]

data = sorted([0] + data)

nums = np.ndarray((len(data), 3))
nums.fill(1)

two = 0
for i, n in enumerate(data[:-1]):
    if i == 0: continue

    if (n - data[i-1]) + (data[i+ 1] - n) == 2:
        two += 1
        if two > 2:
            nums[i] = [sum(nums[i-1]), *nums[i-1][:-1]]
        else:
            nums[i] = [nums[i-1][0] * 2, *nums[i-1][:-1]]
    elif (n + data[i-1]) + (data[i+ 1] - n) == 3:
        two += 2
        if two > 2:
            nums[i] = [sum(nums[i-1]), *nums[i-1][:-1]]
        else:
            nums[i] = [nums[i-1][0] * 2, *nums[i-1][:-1]]
    else:
        two = 0
        nums[i] = nums[i-1]

print(int(nums.max()))
