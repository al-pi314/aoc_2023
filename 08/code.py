from functools import reduce
from math import lcm

with open("input.txt", "r") as file:
    # Part 1
    # start = 'AAA'
    # end = 'ZZZ'
    
    # Part 2
    start = 'A'
    end = 'Z'

    # Read Directions
    direction = list(file.readline().strip()) 
    file.readline()

    # Read Graph Structure
    graph = {}
    current = []
    for line in file.readlines():
        data = line.split(" = ")
        node = data[0]
        graph[node] = data[1].replace("(", "").replace(")", "").strip().split(", ")
        if node.endswith(start):
            current.append(node)
    
    # Find the first cycle
    # It is not stated in the instructions but there always will be a cycle that ends on an end node
    # Than we can just use LCM of all cycle lengths to calculate when they will all reach the end
    # But this should not be the general solution as per problem statment
    visited = [{} for _ in current]
    cycle_length = [-1 for _ in current]
    step = 0
    while any([l == -1 for l in cycle_length]):
        for i in range(len(current)):
            if cycle_length[i] != -1:
                continue
            rel_step = step % len(direction)
            k = (current[i], rel_step)
            if k in visited[i]:
                cycle_length[i] = len(visited[i]) - visited[i][k]
                continue
            visited[i][k] = rel_step
            current[i] = graph[current[i]][direction[rel_step] == 'R']
        step += 1
    print(reduce(lcm, cycle_length))