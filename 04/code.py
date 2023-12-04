import re

with open("input.txt", "r") as file:
    points = 0
    sracthers_by_id = {}
    for i, line in enumerate(file.readlines()):
        line = re.sub(r"\s+", " ", line).split(": ")[1].split(" |")
        winning = set(line[0].strip().split(" "))
        my = set(line[1].strip().split(" "))
        winning_cards = len(winning.intersection(my))
        sracthers_by_id[i] = sracthers_by_id.get(i, 0) + 1
        if winning_cards == 0:
            continue
        points += 2**(winning_cards-1)
        for j in range(i + 1, i + winning_cards + 1):
            sracthers_by_id[j] = sracthers_by_id.get(j, 0) + sracthers_by_id[i]
    print(points)
    print(sum(sracthers_by_id.values()))