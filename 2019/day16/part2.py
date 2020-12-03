import datetime

import numpy as np


# start = "597935135167823748259152439938228652036882987219193396282745877757050067284279217514305" \
#         "335109813433237585769854374518677529360521531927536604639741468421691695040667304748765" \
#         "870166688261246390109223912189067073766629192049805836719613742437133621702772311016865" \
#         "740782217919654581647859253844861275081732395633728337768416062712376947689388317091364" \
#         "533543217083198350836662239566182729812946314699546247606204121700693963833356804282143" \
#         "995230300646012636762709032139969564142873362346829038598236759581550099873842025944091" \
#         "759303847367604166424567849090430494718281431678530960888243394259889072925587074807254" \
#         "10676823614387254696304038713756368483311"

start = "80871224585914546619083218645595"


start_list = np.array([[int(str_num) for str_num in start] for _ in range(len(start))])
start_list_copy = start_list.copy()

final_list = []


def change_pattern(base: list, current: list):
    iter = 0

    for num in base:
        current.insert(current[iter:].index(num) + iter, num)
        while current[iter] == num and num != base[-1]:
            iter += 1

    return current


# phases = 100

if __name__ == '__main__':

    base = [0, 1, 0, -1]
    base_edit = base.copy()

    final = []
    step = []

    row_col = len(start_list[0])

    # row_col =
    # row_col = 100

    for _ in range(row_col):
        step += base_edit
        step.pop(0)
        while row_col > len(step):
            step += base_edit

        final.append(step[:row_col].copy())
        step.clear()
        base_edit = change_pattern(base, base_edit)

    coeffs = np.array(final)
    print('-------')

    a = datetime.datetime.now()

    for _ in range(4):
        print(_)

        product_arr = (start_list * coeffs)

        answer_str = list(map(lambda x: str(x)[-1], product_arr.sum(axis=1)))

        new = list(map(lambda x: int(x), answer_str))
        # str(coeffs)
        # print(*map(lambda x: np.array2string(x, max_line_width=1000), coeffs), sep='\n')
        # print("\n\n------------------------------\n\n")
        # print(*map(lambda x: np.array2string(x, max_line_width=1000), start_list), sep='\n')
        # print("\n\n------------------------------\n\n")
        # print(product_arr.sum(axis=0))
        # print("\n\n------------------------------\n\n")
        # print(coeffs[0], start_list[0], (coeffs[0]*start_list[0]), (coeffs[0]*start_list[0]).sum(), sep="\n")


        start_list = [new for _ in range(row_col)]


    final = ''.join(list(map(lambda x: str(x), new)))
    print(final[:8])
    print(final)

    print(datetime.datetime.now() - a)
    # print(*start_list_copy[:8], sep="")


# 0:00:43.961142
# 0:00:40.763319 <- calling less methods
# 0:01:31.661233 <- bad implementation of numpy
# 0:00:24.918776 <- numpy

