import re

def parse_input(file, part2=False):
    with open(file) as f:
        lines = f.read().splitlines()

    seedline = [int(a) for a in lines[0][6:].split(' ') if a != '']
    
    map_index = []
    for i,l in enumerate(lines):
        if '-to-' in l:
            map_index.append(i)

    return lines, map_index, seedline

def input_seed_range(seedline, part2=False):
    if part2:
        smin = None
        smax = None

        for i in range(0, len(seedline), 2):
            a = seedline[i]
            b = a + seedline[i+1]

            if not smin: smin = a
            if not smax: smax = b

            if a < smin: smin = a
            if b > smax: smax = b
        return smin, smax 
 
    else:
        return min(seedline), max(seedline)

def source_range_from_map(lines, i):
    input_ranges = []
    while True:
        i += 1
        if lines[i] == '':
            break
        else:
            dest, source, n = [int(a) for a in lines[i].split(' ') if a != '']
        
        diff = dest - source
        in_range = source + n
        input_ranges.append((source, in_range, diff))
    return input_ranges
        



lines, map_index, seedline = parse_input('05-sample.txt')

# print(input_seed_range(seedline))
# print(input_seed_range(seedline, part2=True))
print(source_range_from_map(lines, 2))