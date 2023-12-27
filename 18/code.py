from bisect import insort
from itertools import product

with open("input.txt", "r") as file:
    swap = True
    x = 0
    y = 0
    lines = []
    for line in file.readlines():
        d, l, c = line.strip().split(" ")
        if swap:
            d = [(1, 0), (0, 1), (-1, 0), (0, -1)][int(c[-2])]
            l = int(c[2:-2], 16)
        else:
            d = {'R':(1, 0), 'D':(0, 1), 'L':(-1, 0), 'U':(0, -1)}[d]
            l = int(l)

        ex = x + d[0] * l
        ey = y + d[1] * l
        if d[0] != 0:
            lines.append((y, min(x, ex), max(x, ex)))
        x = ex
        y = ey

    def intersect(l1, l2):
        return l1[1] <= l2[1] <= l1[2] or l1[1] <= l2[2] <= l1[2]
        
    size = 0
    lines.sort()
    visited = set()
    while len(lines) > 0:
        l = lines.pop(0)
        
        for i, e in enumerate(lines):
            if intersect(l, e):
                break
        lines.pop(i)
        size += (l[2] - l[1] + 1) * (e[0] - l[0] + 1)
        
        if l[1] != l[2] and (l[1] == e[2] or l[2] == e[1]):
            insort(lines, e)
            if l[1] == e[2]:
                size -= (1 if l[0] == e[0] else l[2] - l[1] + 1)
                insort(lines, (e[0], l[1] + 1, l[2]))
            elif l[2] == e[1]:
                size -= (1 if l[0] == e[0] else l[2] - l[1] + 1)
                insort(lines, (e[0], l[1], l[2] - 1))
        else:
            if l[1] < e[1]:
                size -= (e[1] - l[1] + 1)
                insort(lines, (e[0], l[1], e[1]))
            if l[2] > e[2]:
                size -= (l[2] - e[2] + 1)
                insort(lines, (e[0], e[2], l[2]))
            if l[1] > e[1]:
                insort(lines, (e[0], e[1], l[1] - 1))
            if l[2] < e[2]:
                insort(lines, (e[0], l[2] + 1, e[2]))
                
    print(size)    