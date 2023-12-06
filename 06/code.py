import re

with open("input.txt", "r") as file:
    times = re.sub(r"\s+", " ", file.readline()).split(":")[1].strip().split(" ")
    distances = re.sub(r"\s+", " ", file.readline()).split(":")[1].strip().split(" ")

    def options(t, d):
        # x = the time we hold the button (and our speed)
        # (t - x) = remaining time     
        # (t - x) * x = distance traveled (remaining time * speed)
        # (t - x) * x > d
        #
        # -x**2 + t * x - d > 0 (two solutions)
        # 0 <= x <= T (restriction for x1, x2)
        low = max(int((- t + (t**2 - 4 * d) ** 0.5) / -2), 0) # low = x1
        high = min(int((- t - (t**2 - 4 * d) ** 0.5) / -2), t) # high = x2

        # we can hold the button anywhere in range from low to high
        return high - low
    
    # Part 1
    ans = 1
    for t, d in zip(times, distances):
        ans *= options(int(t), int(d))
    print(ans)

    # Part 2
    print(options(int("".join(times)), int("".join(distances))))