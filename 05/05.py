import re

def parse_input(file, part2=False):
    with open(file) as f:
        lines = f.read().splitlines()

    seedline = lines[0][6:]
    
    map_index = []
    for i,l in enumerate(lines):
        if '-to-' in l:
            map_index.append(i)

    return lines, map_index, seedline

    
def location_for_all_seeds(lines, map_index, seedline, part2=False):
    seeds = [int(a) for a in seedline.split(' ') if a != '']
    if not part2:

        locmin = None
        for s in seeds:
            loc = location_for_one_seed(lines, map_index, s)
            if not locmin:
                locmin = loc
            elif loc < locmin:
                locmin = loc
        return locmin
    
    else:
        locmin = None
        for i in range(0, len(seeds), 2):
            for s in range(seeds[i], seeds[i] + seeds[i+1]+1):
                
                loc = location_for_one_seed(lines, map_index, s)
                if not locmin:
                    locmin = loc
                elif loc < locmin:
                    locmin = loc
        return locmin
    

def location_for_one_seed(lines, map_index, seed):
    next_input = seed
    # print('seed', next_input)
    for i in map_index:
        next_input = parse_input_output(next_input, lines, i)
        # print(f'\t{next_input}')
    return next_input


def parse_input_output(source, lines, i):
    j = 1
    while True:
        try:
            current_map = lines[i+j]
        except IndexError:
            break

        if current_map == '': break

        dest_range, source_range, n = [int(a) for a in current_map.split(' ') if a != '']

        diff = (source - source_range)
        if diff <= n and diff >= 0:
            return dest_range + diff
        else:
            j += 1
            continue
    return source
    
    return output
lines, map_index, seedline = parse_input('05-input.txt')
# print(seeds)
locmin = location_for_all_seeds(lines, map_index, seedline)
# print(locs)
print('Part 1:', locmin)

lines, map_index, seedline = parse_input('05-input.txt')
# print(len(seedline))
locmin = location_for_all_seeds(lines, map_index, seedline, part2=True)
# print(locs)
print('Part 2:', locmin)

