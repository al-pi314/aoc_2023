from collections import deque

with open("input.txt", "r") as file:
    direction = list(file.readline().strip()) 
    file.readline()

    start = 'A'
    end = 'Z'
    current = []

    graph = {}
    for line in file.readlines():
        data = line.split(" = ")
        node = data[0]

        connections = data[1].replace("(", "").replace(")", "").strip().split(", ")
        graph[node] = connections

        if node.endswith(start):
            current.append(node)

    def find_ends(node, i, visited):
        rel_i = i % len(direction)
        print(node, rel_i)
        if (node, rel_i) in visited:
            print("loop:", i - visited[(node, rel_i)])
            return
        visited[(node, rel_i)] = i

        if node.endswith(end):
            print("end", i)
        
        d = 0 if direction[rel_i] == 'L' else 1
        find_ends(graph[node][d], i+1, visited)
    
    find_ends('ZZZ', 0, {})
