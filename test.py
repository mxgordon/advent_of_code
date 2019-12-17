from day16.part1 import change_pattern, np


base = [0, 1, 0, -1]
base_edit = base.copy()

final = []
step = []

colums = 100
rows = 200


for _ in range(rows):

    while colums > len(step):
        step += base_edit

    final.append(step[:colums].copy())
    step.clear()
    base_edit = change_pattern(base, base_edit)

coeffs = np.array(final)

print(len(coeffs))

