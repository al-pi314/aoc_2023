import re
from functools import reduce

with open("input.txt", "r") as f:
    restrictions = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    ans_01 = 0
    ans_02 = 0
    for line in f.readlines():
        line = re.sub(r"[:|,|;]", "", line)
        data = line.split()
        game_id = int(data[1])

        valid = True # part 1
        max_value = {w: 0 for w in restrictions} # part 2
        for i, word in enumerate(data):
            if word in restrictions:
                value = int(data[i - 1])
                if value > restrictions[word]:
                    valid = False 
                if value > max_value[word]:
                    max_value[word] = value

        if valid:
            ans_01 += game_id
        
        ans_02 += reduce(lambda x, y: x * y, max_value.values(), 1)
    print(ans_01)
    print(ans_02)