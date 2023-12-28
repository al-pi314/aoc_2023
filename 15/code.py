from collections import defaultdict
from functools import cache

with open("input.txt", "r") as file:
    line = file.readline().strip()
    init_strings = line.split(",")

    @cache
    def hash(s):
        return sum([ord(c) * 17**(len(s)-i) for i, c in enumerate(s)]) % 256
    
    # Part 1
    print("Part 1:", sum([hash(s) for s in init_strings]))

    # Part 2
    # Stores boxes by hash value and in those stores lenses keyed by label. 
    # Lenses are stored in form of tuples. 
    # First value is used for sorting and is equal to the 'i' value when the lense was first added to the box
    # Second value is used for calculations and is the lenses focal length
    boxes = defaultdict(lambda: defaultdict(lambda: [i]))
    for i, s in enumerate(init_strings):
        idx = -1 if s[-1] == '-' else -2
        label = s[:idx]
        label_hash = hash(label)

        if s[idx] == "=":        
            boxes[label_hash][label] = (boxes[label_hash][label][0], int(s[idx+1:]))
        else:
            boxes[label_hash].pop(label, None)

    # Calculate focusing power
    # Boxes are simply sorted by their hash value (0-255)
    # Lenses in the boxes are sorted by first tuple value
    # This value is equal to 'i' when the lense was first added
    focusing_power = 0
    for box in sorted(boxes.keys()):
        ordered_box_lenses = sorted(boxes[box].values())
        for i, lense in enumerate(ordered_box_lenses):
            focusing_power += (box + 1) * (i + 1) * lense[-1]
    print("Part 2:", focusing_power)
