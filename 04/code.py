import re

with open("input.txt", "r") as file:
    points = 0 # part 1
    sracthers_by_id = {} # part 2
    for i, line in enumerate(file.readlines()):
        sracthers_by_id[i] = sracthers_by_id.get(i, 0) + 1 # part 2
        
        # assuming no duplicates (does not make sense in context of the problem)
        line = re.sub(r"\s+", " ", line).split(": ")[1].split(" | ")
        winning = set(line[0].split(" "))
        my = set(line[1].split(" "))
        won_cards = len(winning.intersection(my))
        if won_cards == 0:
            continue
        
        points += 1 << (won_cards - 1) # part 1

        # part 2
        for j in range(i + 1, i + won_cards + 1):
            sracthers_by_id[j] = sracthers_by_id.get(j, 0) + sracthers_by_id[i]

    print(points) # part 1
    # assuming no scratchers of id >= len(file.readlines()) are present (as per instructions)
    print(sum(sracthers_by_id.values())) # part 2