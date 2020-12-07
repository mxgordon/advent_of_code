import json


def remove_bag_str(bag):
    return " ".join(bag.split(' ')[:-1])


def get_num_bags(line):
    try:
        num = int(line[0])
        return num, remove_bag_str(line[2:])
    except ValueError:
        return 1, remove_bag_str(line)


with open("data.txt", 'r') as read:
    with open("data.json", 'w') as write:
        data = [line.strip().split(' contain ') for line in read.readlines()]
        data = [[remove_bag_str(line[0]), [get_num_bags(bag) for bag in line[1].split(', ')]] for line in data]
        json.dump(data, write)
