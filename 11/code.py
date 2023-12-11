with open("input.txt", "r") as file:
    galaxies = []
    X = []
    Y = []
    for y, line in enumerate(file.readlines()):
        for x, symbol in enumerate(line.strip()):
            if symbol == '.':
                continue
            galaxies.append((x,y))
            X.append(x)
            Y.append(y)
    X.sort()
    Y.sort()

    offset = 0
    prev = 0
    for x in X:
        if x - prev > 1:
            offset += (x-prev-1) * 2
        print(offset)

    
    
