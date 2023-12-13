import re

with open("input.txt", "r") as file:
    folds = 1 # Part 1
    # folds = 5 # Part 2
    res = 0
    for line in file.readlines():
        spring, groups = line.strip().split(" ")
        groups = list(map(int, groups.split(",")))

        spring = "?".join(folds * [spring])
        groups = folds * groups

        def valid_locations(i, size):
            r = []
            while i < len(spring) and spring[i] == '.':
                i += 1

            if i >= len(spring):
                return 0, -1
            
            l = i
            r = i + size
            
            
            if r > len(spring):
                return 0, -1
            
            if "." in spring[l:r]:
                return valid_locations(l + 1, size)
            
            if not (r == len(spring) or spring[r] != "#"):
                return valid_locations(l + 1, size)

            if spring[l:r] == "#" * size:
                return 1, l

            valid, mandatory = valid_locations(l + 1, size)
            return 1 + valid, mandatory            

        print(spring)
        for g in groups:
            print(g, valid_locations(0, g))
