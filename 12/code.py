import re

with open("input.txt", "r") as file:
    res = 0
    for line in file.readlines():
        spring, groups = line.strip().split(" ")
        spring = list(spring)
        groups = list(map(int, groups.split(",")))

        def valid_locations(g):
            r = []
            i = 0
            while i < len(spring):
                size = 0
                while i < len(spring) and size < g:
                    size = size + 1 if spring[i] != '.' else 0
                    size = min(size, g)
                    if size == g and i - size >= 0 and spring[i - size] == "#":
                        size -= 1
                    if size == g and i + 1 < len(spring) and spring[i + 1] == "#":
                        size -= 1
                    i += 1
                if i < len(spring):
                    r.append(i - g)
                    i = i - g + 1
                elif i == len(spring) and size == g and spring[i - g - 1] != '#':
                    r.append(i - g)
            return r
        
        locations = []
        for g in groups:
            locations.append(valid_locations(g))

        def arrangments(gi, last):
            if gi >= len(groups):
                return 1
            
            a = 0
            for l in locations[gi]:
                if l - 1 < last:
                    continue
                a += arrangments(gi+1, l+groups[gi])
            return a
        
        a =  arrangments(0, -1)
        res += a
    print(res)

            
