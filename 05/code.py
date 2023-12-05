with open("input.txt") as f:
    # Input
    seeds = list(map(lambda x: int(x), f.readline().split(": ")[1].strip().split(" ")))

    # Transform input for challange parts:
    # seeds = [(s, 1) for s in seeds] # Part 1
    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)] # Part 2

    transformed = set() # we want to avoid transforming the same seed with the same map twice
    for line in f.readlines():
        line = line.strip()
        # empty lines hold no information
        if line == "":
            continue
        
        # new map starts
        if line[-1] == ":":
            transformed = set() # reset transformations
            continue
        
        # transformation
        destination, source, length = list(map(lambda x: int(x), line.split(" ")))
        i = 0
        # source interval denoted as ()
        # range interval denoted as []
        nseeds = []
        ntransformed = set()
        while i < len(seeds):
            # interval was already transformed by current map
            if i in transformed:
                ntransformed.add(len(nseeds))
                nseeds.append(seeds[i])
                i += 1
                continue            

            range_start, range_length = seeds[i]
            # case 0: [] () or () []
            if range_start + range_length <= source or range_start >= source + length:
                nseeds.append(seeds[i])
            # case 1: ( [
            elif range_start >= source and range_start < source + length:
                offset = range_start - source
                inside_length = min(length - offset, range_length)

                # transform the part inside of ( )
                ntransformed.add(len(nseeds))
                nseeds.append((destination + offset, inside_length))

                # copy the part outside of ( )
                if inside_length < range_length:
                    seeds.append((range_start + inside_length, range_length - inside_length))
            # case 2: [ ( 
            elif range_start < source and range_start + range_length > source:
                offset = source - range_start
                inside_length = min(length, range_length - offset)

                # transform the part inside of ( )
                ntransformed.add(len(nseeds))
                nseeds.append((destination, inside_length))

                # copy the part before the (
                if offset > 0: 
                    seeds.append((range_start, offset))

                # copy the part outside of ( )
                if inside_length + offset < range_length:
                    seeds.append((source + length, range_length - inside_length - offset))
            else:
                # make sure that if statements cover all cases
                raise TypeError("missed condition", range_start, range_length, source, length)
            
            i += 1
        # overwrite with new data
        seeds = nseeds
        transformed = ntransformed

    # Result is the smallest start of an interval   
    print("Size:", len(seeds))         
    print("Result:", min(seeds)[0])
