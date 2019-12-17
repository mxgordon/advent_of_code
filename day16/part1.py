start = "597935135167823748259152439938228652036882987219193396282745877757050067284279217514305" \
        "335109813433237585769854374518677529360521531927536604639741468421691695040667304748765" \
        "870166688261246390109223912189067073766629192049805836719613742437133621702772311016865" \
        "740782217919654581647859253844861275081732395633728337768416062712376947689388317091364" \
        "533543217083198350836662239566182729812946314699546247606204121700693963833356804282143" \
        "995230300646012636762709032139969564142873362346829038598236759581550099873842025944091" \
        "759303847367604166424567849090430494718281431678530960888243394259889072925587074807254" \
        "10676823614387254696304038713756368483311"

# start = "80871224585914546619083218645595"

start_list = [int(str_num) for str_num in start]
start_list_copy = start_list.copy()
current_pattern = [0, 1, 0, -1]
pattern = current_pattern.copy()

final_list = []


def change_pattern(base: list, current: list):
    iter = 0

    for num in base:
        current.insert(current[iter:].index(num) + iter, num)
        while current[iter] == num and num != base[-1]:
            iter += 1

    return current

phases = 100

if __name__ == '__main__':
    for _ in range(phases):
        print(_)
        for j in range(len(start_list)):

            start_list = start_list_copy.copy()
            for i in range(len(start_list)):

                index = (len(start_list) - (len(start_list)) % len(current_pattern) + i + 1) % len(current_pattern)

                tmp_set = start_list[i] * current_pattern[index]

                start_list[i] = tmp_set

            tmp_set = int(str(sum(start_list))[-1])

            final_list.append(tmp_set)

            current_pattern = change_pattern(pattern, current_pattern)

        start_list_copy = final_list.copy()
        final_list.clear()
        current_pattern = pattern.copy()

    print(*start_list_copy[:8], sep="")




