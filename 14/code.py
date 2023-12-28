from functools import reduce

with open("input.txt", "r") as file:
    # read rocks and anchors as a list of points
    rocks = []
    anchors = []
    for y, line in enumerate(file.readlines()):
        for x, c in enumerate(line.strip()):
            if c == 'O':
                rocks.append((x, y))
            elif c == "#":
                anchors.append((x, y))
    
    # add anchors
    height = y + 1
    width = x + 1
    # on top and bottom
    for x in range(width):
        anchors.append((x, -1))
        anchors.append((x, height))

    # on left and right
    for y in range(height):
        anchors.append((-1, y))
        anchors.append((width, y))

    # sort rocks and anchors for slide logic to work
    rocks.sort()
    anchors.sort()
    
    # slides all the rocks
    def slide(R, A):
        ai = 0
        for i, rock in enumerate(R):
            while A[ai][0] != rock[0]:
                ai += 1

            while A[ai+1][1] < rock[1]:
                ai += 1
            
            y = A[ai][1] + 1
            if i != 0 and R[i-1][0] == rock[0]:
                y = max(y, R[i-1][1] + 1)
            R[i] = (rock[0], y)
        return R
    
    def north_to_east(arr):
        return sorted([(e[1], e[0]) for e in arr])
    
    def east_to_south(arr):
        return sorted([(e[1], -e[0]) for e in arr])
    
    def south_to_west(arr):
        return sorted([(-e[1], -e[0]) for e in arr])
    
    def west_to_north(arr):
        return sorted([(-e[1], e[0]) for e in arr])
    
    # would_anchor = set()
    # def anchor_rocks(oR, R, A):
    #     global would_anchor
    #     by_c = {}
    #     by_r = {}

    #     for r in R:
    #         by_c[r[0]] = by_c.get(r[0], []) + [r]
    #         by_r[r[1]] = by_r.get(r[1], []) + [r]

    #     for changed in set(oR).symmetric_difference(set(R)):
    #         by_c.pop(changed[0], None)
    #         by_r.pop(changed[1], None)
        
    #     v_by_c = set()
    #     for v in by_c.values():
    #         v_by_c = v_by_c.union(set(v))

    #     v_by_r = set()
    #     for v in by_r.values():
    #         v_by_r = v_by_r.union(set(v))

    #     unchanged = v_by_c.intersection(v_by_r)
    #     if len(would_anchor) > 0 and len(would_anchor - unchanged) > 0:
    #         print(would_anchor)
    #         print(would_anchor-unchanged)
    #         print("DANGER")
    #     would_anchor = would_anchor.union(unchanged)
    #     return R, A

    def load(R, A):
        load = 0
        for r in R:
            load += (height - r[1])
        
        original_A = set(anchors)
        for a in A:
            if a not in original_A:
                load += (height - a[1])
        return load
    
    def spin(R, A, spins):
        for i in range(spins):
            oR = set(R.copy())

            R = slide(R, A)
            if i == 0:
                print(load(R, A))
            A = north_to_east(A)
            R = north_to_east(R)

            R = slide(R, A)
            A = east_to_south(A)
            R = east_to_south(R)

            R = slide(R, A)
            A = south_to_west(A)
            R = south_to_west(R)

            R = slide(R, A)
            A = west_to_north(A)
            R = west_to_north(R)

            # R, A = anchor_rocks(oR, R, A)
            # if len(R) == 0:
            #     break
            print(set(R).symmetric_difference(oR))
            if set(R) == oR:
                print("Equal")
                break

        print(load(R, A))
        return R, A
    print(len(rocks))
    R, A = spin(rocks, anchors, 10000000000)

    # Draw
    fixed_anchors = set(anchors)
    fixed_rocks = set([tuple(r) for r in R])
    locked_rocks = set(A) - fixed_anchors
    for y in range(height):
        for x in range(width):
            if (x, y) in fixed_rocks:
                print("O", end="")
            elif (x, y) in fixed_anchors:
                print("#", end="")
            elif (x, y) in locked_rocks:
                print("X", end="")
            else:
                print(".", end="")
        print()