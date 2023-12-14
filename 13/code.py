import numpy as np

with open("input.txt", "r") as file:
    # smudges = 0 # Part 1
    smudges = 1 # Part 2

    def reflection_indexes(arr):
        r = 0 
        for i in range(1, arr.shape[0]):
            o = min(i-1, arr.shape[0]-i-1)
            size = (o+1) * arr.shape[1]
            if (arr[i-1-o:i, :] == np.flip(arr[i:i+o+1], axis=0)).sum() == size - smudges:
                r += i
        return r
    
    def reflections(arr):
        return 100 * reflection_indexes(arr) + reflection_indexes(arr.T)
        
    r = 0
    data = []
    for line in file.readlines():
        line = line.strip()
        if line == "":
            r += reflections(np.array(data))
            data = []
            continue
        data.append(list(map(lambda x: 0 if x == "." else 1, line)))
        
    r += reflections(np.array(data))
    print(r)
