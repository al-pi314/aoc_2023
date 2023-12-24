from collections import deque

with open("input.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

    def coverage(starting_beam):
        beams = deque([starting_beam])
        visited = set()
        pos_visited = set()
        while len(beams) > 0:
            dx, dy, x, y = beams.popleft()

            if y < 0 or y >= len(grid):
                continue
            
            if x < 0 or x >= len(grid[y]):
                continue

            if (dx, dy, x, y) in visited:
                continue
            visited.add((dx, dy, x, y))
            pos_visited.add((x, y))
                
            s = grid[y][x]
            # pass
            if s == '.':
                beams.append((dx, dy, x + dx, y + dy))
                continue
            
            # split vertically
            if s == '|':
                if dx == 0:
                    beams.append((dx, dy, x, y + dy))
                    continue
                
                beams.append((0, 1, x, y + 1))
                beams.append((0, -1, x, y - 1))
                continue
            
            # split horizontally
            if s == '-':
                if dy == 0:
                    beams.append((dx, dy, x + dx, y))
                    continue
                
                beams.append((1, 0, x + 1, y))
                beams.append((-1, 0, x - 1, y))
                continue
            
            # reflect /
            if s == '/':
                beams.append((-dy, -dx, x - dy, y - dx))
                continue
            
            # reflect \
            if s == '\\':
                beams.append((dy, dx, x + dy, y + dx))
                continue

        return len(pos_visited)
    
    m = coverage((1, 0, 0, 0))
    print("Part 1:", m)
    for i in range(len(grid)):
        m = max(m, coverage((1, 0, 0, i))) # from left to right
        m = max(m, coverage((-1, 0, len(grid[i]) - 1, i))) # from right to left
    for j in range(len(grid[0])):
        m = max(m, coverage((0, 1, j, 0))) # top to bottom
        m = max(m, coverage((0, -1, j, len(grid) - 1))) # bottom to top
    print("Part 2:", m)
        