from collections import deque

with open("input.txt", "r") as file:
    direction = list(file.readline().strip()) 
    file.readline()

    start = 'A'
    end = 'Z'
    origins = []

    graph = {}
    for line in file.readlines():
        data = line.split(" = ")
        node = data[0]

        connections = data[1].replace("(", "").replace(")", "").strip().split(", ")
        graph[node] = connections

        if node.endswith(start):
            origins.append(node)

    def loop(node, i, visited):
        rel_i = i % len(direction)
        k = (node, rel_i)
        print(k)
        if k in visited:
            print("loop", visited[k])
            return
        visited[k] = i
        
        d = 0 if direction[rel_i] == 'L' else 1
        loop(graph[node][d], i + 1, visited)
    
    loop('ZZZ', 0, {})