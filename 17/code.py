import heapq

import numpy as np

with open("input.txt", "r") as file:
    grid = np.array(list(list(map(int, list(line.strip()))) for line in file.readlines()))
    min_step = 4
    max_step = 10

    visited = set()
    q = []
    heapq.heappush(q, (0, 0, 0, 0, 1, 0))
    while len(q) > 0:
        # unpack the task
        hl, s, x, y, dx, dy = heapq.heappop(q)

        # end check
        if y == grid.shape[0] - 1 and x == grid.shape[1] - 1 and s >= min_step:
            print("Part 1:", hl)
            break
        
        # valid directions
        d = set([(-1, 0), (1, 0), (0, -1), (0, 1)])
        d.remove((-dx, -dy)) # going backwards is not allowed
        if s == max_step:
            d.remove((dx, dy)) # after 3 steps we must swithc direction
        if s < min_step:
            d = set([(dx, dy)])

        # add all valid directions to the queue
        for (ndx, ndy) in d:
            nx = x + ndx
            ny = y + ndy
            if ny < 0 or ny >= grid.shape[0]:
                continue
            if nx < 0 or nx >= grid.shape[1]:
                continue

            ns = 1 if (dx, dy) != (ndx, ndy) else s + 1
            nhl = hl + grid[min(y, ny):max(y, ny)+1, min(x, nx):max(x, nx)+1].sum() - grid[y][x]

            if (nx, ny, ndx, ndy, ns) in visited:
                continue
            visited.add((nx, ny, ndx, ndy, ns))
            heapq.heappush(q, (nhl, ns, nx, ny, ndx, ndy))
