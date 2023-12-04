visited = {}
def part_number(x, y):
    if y < 0 or y >= len(engine):
        return None
    if x < 0 or x >= len(engine[y]):
        return None
    if not engine[y][x].isnumeric():
        return None
    if x in visited.get(y, set()):
        return None
    
    while x > 0 and engine[y][x - 1].isnumeric():
        x -= 1
    
    number = 0
    while x < len(engine[y]) and engine[y][x].isnumeric():
        visited[y] = visited.get(y, set()) | {x}
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
            
            parts = []
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    pn = part_number(x + dx, y + dy)
                    if pn is not None:
                        parts.append(pn)
                
            ans_part_one += sum(parts)
            if len(parts) == 2 and engine[y][x] == "*":
                ans_part_two += parts[0] * parts[1]

    print(ans_part_one)
    print(ans_part_two)
    