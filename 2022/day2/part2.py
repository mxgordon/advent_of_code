with open("data.txt", 'r') as f:
    data = f.readlines()

data = [d.split() for d in data]

score_list = {"X": 0, "Y": 3, "Z": 6}
tie = {"A": 1, "B": 2, "C": 3}
lose = {"A": 3, "B": 1, "C": 2}
win = {"A": 2, "B": 3, "C": 1}
decider = {"X": lose, "Y": tie, "Z": win}

scores = []

for them, outcome in data:
    scores.append(score_list[outcome])
    scores[-1] += decider[outcome][them]

print(sum(scores))
