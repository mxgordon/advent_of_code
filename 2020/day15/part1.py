data = list(map(int, "9,12,1,4,17,0,18".split(',')))

nums = []

for i in range(2020):
    if i < len(data):
        nums.append(data[i])
    elif i == len(data):
        nums.append(0)
    else:
        last = nums[-1]
        try:
            spoken = nums[::-1].index(last, 1)
        except ValueError:
            spoken = 0
        nums.append(spoken)
print(nums)
