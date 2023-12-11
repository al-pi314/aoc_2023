def differences(seq):
    return [seq[i+1] - seq[i] for i in range(len(seq)-1)]

with open("input.txt", "r") as file:
    p1 = 0
    p2 = 0
    for line in file.readlines():
        seq = list(map(int, line.split(" ")))
        l = len(seq)
        future = seq[-1]
        past = seq[0]
        while not all([v == 0 for v in seq]):
            seq = differences(seq)
            future += seq[-1]
            past += (-1)**(l - len(seq)) * seq[0]
        p1 += future
        p2 += past
    print(p1)
    print(p2)
