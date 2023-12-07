from collections import Counter


def hand(h, b, jokers=False):
    h_count = Counter(h) # count how many times each card repeats
    wild_cards = 0 if not jokers or 1 not in h_count else h_count.pop(1) # number of wild cards if allowed else 0
    
    # increase the highest card count by the number of wild cards as this improves the hand the most
    counts = sorted(h_count.values())
    counts.append(wild_cards if len(counts) == 0 else counts.pop(-1) + wild_cards)

    # count how many times the same count appears
    counts_count = Counter(counts)
    strength = [counts_count.get(hs, 0) for hs in range(5, 0, -1)]
    return tuple(strength + h + [b])
    

with open("input.txt","r") as file:
    # jokers = False # Part 1
    jokers = True # Part 2

    letter_map = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    letter_map['J'] = 11 if not jokers else 1

    hands = []
    for line in file.readlines():
        # parsing
        h, b = line.strip().split(" ")
        h = h if not jokers else h.replace('J', '1') # jokers value becomes one
        h = list(map(lambda x: int(x) if x.isdigit() else letter_map[x], list(h))) # convert cards to their value
        b = int(b)

        # construct a hand
        hands.append(hand(h, b, jokers=jokers))
    # hands are constructed in such a way that they can be sorted according to the rules
    hands.sort()

    # answer is hands' ranking multiplied by its bid
    ans = 0
    for i, h in enumerate(hands):
        ans += (i+1) * h[-1]
    print(ans)


    