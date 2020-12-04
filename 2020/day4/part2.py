import json


with open("data.json", 'r') as f:
    data = json.load(f)


def valid_hex(letters):
    if letters[0] != "#":
        return False
    letters = letters[1:]
    if len(letters) != 6:
        return False
    for l in letters:
        if l not in [*'12344567890abcdef']:
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
for d in data:
    if len(d) == 8 or (len(d) == 7 and 'cid' not in d):
        if not 1920 <= int(d['byr']) <= 2002:
            pass
        elif not 2010 <= int(d['iyr']) <= 2020:
            pass
        elif not 2020 <= int(d['eyr']) <= 2030:
            pass
        elif d['hgt'][-2:] == 'in' and not 59 <= int(d['hgt'][:-2]) <= 76:
            pass
        elif d['hgt'][-2:] == 'cm' and not 150 <= int(d['hgt'][:-2]) <= 193:
            pass
        elif d['hgt'][-2:] not in ['cm', 'in']:
            pass
        elif not valid_hex(d['hcl']):
            pass
        elif not has_nine_num(d['pid']):
            pass
        elif d['ecl'] not in 'amb blu brn gry grn hzl oth'.split():
            pass
        else:
            valid += 1

print(valid)
