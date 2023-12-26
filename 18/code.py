from collections import deque

with open("input.txt", "r") as file:
    # swap = False # Part 1
    swap = True # Part 2

    H_to_D = {
        '0': 'R',
        '1': 'D',
        '2': 'L',
        '3': 'U',
    }
    D = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, -1),
        'D': (0, 1),
    }
    
    dug = set([(0, 0)])
    x = 0
    y = 0

    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for line in file.readlines():
        d, l, c = line.strip().split(" ")
        if swap:
            d = H_to_D[c[-2]]
            l = str(int(c[2:-2], 16))

        d = D[d]
        l = int(l)      

        for _ in range(l):
            x += d[0]
            y += d[1]
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            dug.add((x, y))


    visited = set()
    q = deque([(1, 1)])
    size = 0
    while len(q) > 0:
        x, y = q.popleft()
        if y < min_y or y > max_y:
            continue
        
        if x < min_x or x > max_x:
            continue
                
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) in dug:
            continue

        size += 1
        for (nx, ny) in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            q.append((nx, ny))


    # for y in range(min_y, max_y +1):
    #     for x in range(min_x, max_x +1):
    #         if (x, y) in dug:
    #             print("#", end="")
    #         elif (x, y) in visited:
    #             print('x', end="")
    #         else:
    #             print(".", end="")
    #     print()
            
    print(size + len(dug))