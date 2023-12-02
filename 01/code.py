with open("input.txt", "r") as file:
    ans = 0
    # part 1
    # digits = {} 
    # part 2
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    for line in file.readlines():
        first = None
        last = None
        for i, c in enumerate(line):
            for d in digits:
                if line[i:i+len(d)] == d:
                    c = digits[d]
            if c.isnumeric():
                if first is None:
                    first = c
                last = c
        ans += 10 * int(first) + int(last)
    print(ans)