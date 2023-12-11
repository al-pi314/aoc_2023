# Try this example with start_left=True and start_left=False (with draw = True) to see the difference
# ..F7.
# .....
# S---7.
# L-7-|.
# ..L-J.

# More Manual Examples:
# .F--7
# FJ..|
# S|--|
# L-7.|
# F-JFJ
# L7.L7
# .|F-J
# .LJ..

from collections import deque
from itertools import product

with open("input.txt", "r") as file:
    # changes the direction that we follow around the main loop
    # this changes what tiles are included in tiles set (in one case it will be the tiles deemed 'inside' in the other it will be 'outside' tiles)
    # we cannot know in advance what is inside and outside of the loop but the code works in both cases
    # this is mostly useful for debugging
    start_left = True 
    # draws the end grid with some info
    # * for tiles in the main loop
    # inside variable tells us if detected tiles are outside or inside (only one of those are draw)
    # O if found tiles are outside, 
    # I if found tiles are inside
    # . for other tiles
    # x on adjecient tiles detected next to main loop
    draw = True 

    # construct graph
    graph = {}
    start = None
    for y, line in enumerate(file.readlines()):
        for x, symbol in enumerate(line.strip()):
            if symbol == '.':
                continue
            
            if symbol == 'S':
                start = (x, y)
                continue
            
            connecions = None
            if symbol == '|':
                connecions = [(x, y+1), (x, y-1)]
            elif symbol == '-':
                connecions = [(x-1, y), (x+1, y)]
            elif symbol == 'F':
                connecions = [(x+1,y), (x, y+1)]
            elif symbol == 'J':
                connecions = [(x-1, y), (x, y-1)]
            elif symbol == 'L':
                connecions = [(x+1, y), (x, y-1)]
            elif symbol == '7':
                connecions = [(x-1, y), (x, y+1)]
            else:
                raise ValueError(f'unhandled symbol {symbol}')
            
            graph[(x, y)] = connecions
    height = y
    width = x
    assert start != None # sanity

    # Figure out the starting pipe
    graph[start] = []
    x, y = start
    # Check all surrounding pipes
    for sx in [x-1, x, x+1]:
        for sy in [y-1, y, y+1]:
            # Start position needs to be one of the connections of a pipe
            if start not in graph.get((sx, sy), []):
                continue
            graph[start].append((sx, sy))
    assert len(graph[start]) == 2 # sanity

    # Part 1
    main_loop = set([start]) # all tiles that are part of the main loop
    tiles = set() # all tiles adjecient to the main loop (all on the same side) - we do not know if that side is 'inside' or 'outside' yet
    curr = graph[start][start_left]
    prev = start
    prev_d_direction = (0, 0)
    while curr not in main_loop:
        # Part 1 - iterate over the main pipe loop
        main_loop.add(curr)
        n = graph[curr][0] if graph[curr][0] != prev else graph[curr][1] 
        prev, curr = curr, n

        # Part 2 - check for tiles on the side of the pipe
        d_direction = (-curr[1] + prev[1], curr[0] - prev[0]) # perpendicular vector of the direction
        loc = (curr[0] + d_direction[0], curr[1] + d_direction[1])
        tiles.add(loc)

        # Used at correners to check both valid directions
        if prev_d_direction != d_direction:
            loc = (prev[0] + d_direction[0], prev[1] + d_direction[1])
            tiles.add(loc)

        prev_d_direction = d_direction
    tiles = tiles - main_loop # Remove any added tiles that lay on the main loop
    print("Part 1:", len(main_loop) // 2)

    # Part 2    
    visited = set() # all tiles that are connected to 
    q = deque(tiles)
    inside = True # wether the visited tiles are part of the inside of outside
    D = list(product((-1, 0, 1), (-1, 0, 1)))
    while len(q) > 0:
        x, y = q.popleft()
        if (x, y) in visited or (x, y) in main_loop:
            continue
        if y < 0 or y > height or x < 0 or x > width:
            inside = False # if the tile group is touching the grid bounds the groups must be outside
            continue
        visited.add((x, y))

        for dx, dy in D:
            q.append((x + dx, y + dy))

    total_tiles = (width+1)*(height+1) - len(main_loop) # all junk pipes and dots
    nest_tiles = len(visited) if inside else total_tiles - len(visited) # tiles included in the main loop
    print("Part 2:", nest_tiles)
    
    # Draw
    if draw:
        for y in range(height+1):
            for x in range(width+1):
                if (x, y) in tiles:
                    print("x", end="")
                elif (x, y) in visited:
                    print("I" if inside else "O", end="")
                elif (x, y) in main_loop:
                    print("*", end="")
                else:
                    print(".", end="")
            print()