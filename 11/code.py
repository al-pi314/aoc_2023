class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift_x(self, offset):
        self.x += offset
        return self
    
    def shift_y(self, offset):
        self.y += offset
        return self

    def dist(self, G):
        return abs(self.x - G.x) + abs(self.y - G.y)

with open("input.txt", "r") as file:
    # expansion = 2 # Part 1
    expansion = 1000000 # Part 2

    galaxies_by_x = {}
    galaxies_by_y = {}
    galaxies = []
    for y, line in enumerate(file.readlines()):
        for x, symbol in enumerate(line.strip()):
            if symbol == '.':
                continue
            galaxy = Galaxy(x, y)
            galaxies_by_x[x] = galaxies_by_x.get(x, []) + [galaxy]
            galaxies_by_y[y] = galaxies_by_y.get(y, []) + [galaxy]
            galaxies.append(galaxy)

    # Account for light travel in X
    empty = 0
    prev = 0
    for x in sorted(galaxies_by_x.keys()):
        empty += max(0, x - prev - 1)
        prev = x
        galaxies_by_x[x] = [G.shift_x(empty * (expansion - 1)) for G in galaxies_by_x[x]]
    
    # Account for light travel in Y
    empty = 0
    prev = 0
    for y in sorted(galaxies_by_y.keys()):
        empty += max(0, y - prev - 1)
        prev = y
        galaxies_by_y[y] = [G.shift_y(empty * (expansion - 1)) for G in galaxies_by_y[y]]    

    # Calculate total distance among galaxies
    distance = 0
    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            distance += galaxies[i].dist(galaxies[j])
    print(distance)