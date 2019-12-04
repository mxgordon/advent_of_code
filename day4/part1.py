def check(number):
    num_list = [int(digit) for digit in str(number)]
    assert len(num_list) == 6
    double = False
    increasing = True
    for index, digit in enumerate(num_list):
        if index == 0:
            continue

        if digit == num_list[index - 1]:
            double = True

        if digit < num_list[index - 1]:
            increasing = False

    return increasing and double


start = 156218
number = start
end = 652527
counter = 0

while number <= end:
    if check(number):
        counter += 1
    number += 1
# print(check())
print(counter)