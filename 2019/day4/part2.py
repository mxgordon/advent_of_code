def group(num_list: list):
    final_list = [[num_list.pop(0)]]
    for i in num_list:
        if i == final_list[-1][0]:
            final_list[-1].append(i)
        else:
            final_list.append([i])
    return final_list


def check(number: int):
    num_list = [int(digit) for digit in str(number)]
    assert len(num_list) == 6
    double = any([len(i) == 2 for i in group(num_list.copy())])
    increasing = True

    for index, digit in enumerate(num_list):
        if index == 0:
            continue

        if digit < num_list[index - 1]:
            increasing = False

    return increasing and double


start = 156218
end = 652527
counter = 0

for number in range(start, end):
    if check(number):
        counter += 1

print(counter)
