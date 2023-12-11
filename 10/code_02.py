with open("input.txt", "r") as file:
    tiles = list(list(line.strip()) for line in file.readlines())
    
    def is_nest(x, y):
        if y < 0 or y > len(tiles) or x < 0 or x > len(tiles[y]):
            return False
        if tiles[y][x] != '.':
            return False