# Visited includes cordinates of a number as keys and cordinates of source symbol as value
# The need for stroing source cordinates is to avoid an edge case
# ...100...
# ...*.....
# ...100...
# .....+...
# ...100...
# Where the middle number would only be accessed once, but it should be accessed twice
visited = {}
def part_number(x, y, sx, sy):
    if y < 0 or y >= len(engine):
        return None
    if x < 0 or x >= len(engine[y]):
        return None
    if not engine[y][x].isnumeric():
        return None
    if visited.get((x, y)) == (sx, sy):
        return None
    
    while x > 0 and engine[y][x - 1].isnumeric():
        x -= 1
    
    number = 0
    while x < len(engine[y]) and engine[y][x].isnumeric():
        visited[(x, y)] = (sx, sy)
        number = number * 10 + int(engine[y][x])
        x += 1
    
    return number

with open("input.txt") as file:
    engine = [list(line.strip()) for line in file.readlines()]

    ans_part_one = 0
    ans_part_two = 0
    for y in range(len(engine)):
        for x in range(len(engine[y])):
            if engine[y][x] == "." or engine[y][x].isnumeric():
                continue
            
            # parts around the symbol
            parts = []
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    pn = part_number(x + dx, y + dy, x, y)
                    if pn is not None:
                        parts.append(pn)
                
            ans_part_one += sum(parts)
            if len(parts) == 2 and engine[y][x] == "*":
                ans_part_two += parts[0] * parts[1]

    print(ans_part_one)
    print(ans_part_two)
    