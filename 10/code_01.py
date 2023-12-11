with open("input.txt", "r") as file:
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
    assert start != None

    # figure out starting pipe
    graph[start] = []
    x, y = start
    for sx in [x-1, x, x+1]:
        for sy in [y-1, y, y+1]:
            if start not in graph.get((sx, sy), []):
                continue
            graph[start].append((sx, sy))
    assert len(graph[start]) == 2

    # Part 1
    moves = 0
    visited = set()
    current = [(start, graph[start][0]), (start, graph[start][1])]
    while current[0][0] not in visited:
        for i, (curr, prev) in enumerate(current):
            visited.add(curr)
            n = graph[curr][0] if graph[curr][0] != prev else graph[curr][1] 
            prev, curr = curr, n
            current[i] = (curr, prev)
        moves += 1
    print(moves -1)