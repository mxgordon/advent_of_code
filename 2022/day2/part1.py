with open("data.txt", 'r') as f:
    data = f.readlines()

data = [d.split() for d in data]

score_list = {"X": 1, "Y": 2, "Z": 3}
trans = {"X": "A", "Y": "B", "Z": "C"}
scores = []

for them, me in data:
    scores.append(score_list[me])
    if (them, me) in [("A", "Y"), ("B", "Z"), ("C", "X")]:
        scores[-1] += 6
    elif trans[me] == them:
        scores[-1] += 3

print(sum(scores))
