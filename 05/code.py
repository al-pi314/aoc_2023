with open("input.txt") as f:
    seeds = list(map(lambda x: int(x), f.readline().split(": ")[1].strip().split(" ")))
    source = ""
    destination = ""
    mapped = set()
    for line in f.readlines():
        line = line.strip()
        if line == "":
            continue

        if line.endswith("map:"):
            d = line.split(" ")[0].split("-")
            source = d[2]
            destination = d[0]
            print(source, destination)
            mapped = set()
            continue

        d_start, s_start, map_length = list(map(lambda x: int(x), line.split(" ")))
        print(d_start, s_start, map_length)
        i = 0
        new_seeds = []
        new_mapped = set()
        while i < len(seeds):
            
            start = seeds[i]
            length = seeds[i + 1]
            print(start, length)
            if i in mapped:
                print("mapped")
                new_mapped.add(len(new_seeds))
                new_seeds.append(seeds[i])
                new_seeds.append(seeds[i + 1])
                i += 2
                continue

            if start >= s_start and start < s_start + map_length:
                print("one")
                diff = start - s_start
                limited_length = min(length, map_length - diff)
                new_seeds.append(d_start + diff)
                new_seeds.append(limited_length)
                new_mapped.add(len(new_seeds) - 2)
                if length > limited_length:
                    seeds.append(start + limited_length)
                    seeds.append(length - limited_length)
                i += 2
                continue

            if start < s_start and start + length > s_start:
                print("two")
                diff = s_start - start
                limited_length = min(length - diff, map_length)
                new_mapped.add(len(new_seeds))
                new_seeds.append(d_start)
                new_seeds.append(limited_length)
                if diff > 0:
                    seeds.append(start)
                    seeds.append(diff)
                if length - diff > limited_length:
                    seeds.append(s_start + map_length)
                    seeds.append(length - diff - limited_length)
                i += 2
                continue
            
            print("three")
            new_seeds.append(start)
            new_seeds.append(length)
            i += 2
        seeds = new_seeds
        print(seeds)
        print(new_mapped)
        mapped = new_mapped
            
    ans = float("inf")
    for i in range(0, len(seeds), 2):
        ans = min(ans, seeds[i])
    print(ans)
