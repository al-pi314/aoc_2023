from bisect import insort

with open("input.txt", "r") as file:
    swap = False

    x = 0
    y = 0
    lines = []
    dig_size = 0
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
        if ey == y:
            lines.append((y, min(x, ex), max(x, ex)))
        dig_size += (abs(ex - x) + abs(ey - y))
        y = ey
        x = ex

    def intersect(l1, l2):
        return l1[1] <= l2[1] <= l1[2] or l1[1] <= l2[2] <= l1[2]
    
    size = 0
    lines.sort()
    while len(lines) > 0:
        l = lines.pop(0)

        # merge
        while len(lines) > 0 and lines[0][0] == l[0] and (lines[0][1] == l[2] or lines[0][2] == l[1]):
            e = lines.pop(0)
            l = (l[0], min(l[1], e[1]), max(l[2], e[2]))
        
        # find intersections
        for i, e in enumerate(lines):
            if (l[1] == e[2] or l[2] == e[1]) and (e[1] != e[2]):
                continue
            if intersect(l, e) or intersect(e, l):
                break
        else:
            continue
        
        size += (l[2] - l[1] + 1) * (e[0] - l[0] + 1)
        lines.pop(i)

        if l[1] < e[1]:
            size -= (e[1] - l[1] + 1)
            insort(lines, (e[0], l[1], e[1]))
        if l[2] > e[2]:
            size -= (l[2] - e[2] + 1)
            insort(lines, (e[0], e[2], l[2]))
        if l[1] >= e[1] and l[2] <= e[2]:
            insort(lines, e)        
    print(size)
