import json


with open("data.json", 'r') as f:
    data = json.load(f)


def valid_hex(letters):
    if letters[0] != "#":
        return False
    letters = letters[1:]
    if len(letters) != 6:
        return False
    for letter in letters:
        if letter not in [*'12344567890abcdef']:
            return False
    return True


def has_nine_num(num):
    if len(num) != 9:
        return False
    try:
        int(num)
        return True
    except ValueError:
        return False


valid = 0
for passport in data:
    if len(passport) == 8 or (len(passport) == 7 and 'cid' not in passport):
        if not 1920 <= int(passport['byr']) <= 2002:
            pass
        elif not 2010 <= int(passport['iyr']) <= 2020:
            pass
        elif not 2020 <= int(passport['eyr']) <= 2030:
            pass
        elif passport['hgt'][-2:] == 'in' and not 59 <= int(passport['hgt'][:-2]) <= 76:
            pass
        elif passport['hgt'][-2:] == 'cm' and not 150 <= int(passport['hgt'][:-2]) <= 193:
            pass
        elif passport['hgt'][-2:] not in ['cm', 'in']:
            pass
        elif not valid_hex(passport['hcl']):
            pass
        elif not has_nine_num(passport['pid']):
            pass
        elif passport['ecl'] not in 'amb blu brn gry grn hzl oth'.split():
            pass
        else:
            valid += 1

print(valid)
