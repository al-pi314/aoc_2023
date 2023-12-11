from collections import deque

with open("input.txt", "r") as file:
    direction = list(file.readline().strip()) 
    file.readline()

    start = 'AAA'
    end = 'ZZZ'
    current = []

    graph = {}
    for line in file.readlines():
        data = line.split(" = ")
        node = data[0]

        connections = data[1].replace("(", "").replace(")", "").strip().split(", ")
        graph[node] = connections

        if node.endswith(start):
            current.append(node)
    
    print(len(graph))
    
    i = 0
    steps = 0
    while not all([n.endswith(end) for n in current]):
        next = []
        d = 0 if direction[i] == 'L' else 1
        for n in current:
            next.append(graph[n][d])
        i = (i+1) % len(direction)
        current = next
        steps += 1
    print(steps)
