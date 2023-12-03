import re
import numpy as np
import itertools 

input_path = './03-input.txt'


def find_gears(lines):
    '''This function finds all gears (not `.` or a digit)

    Input: list of input lines
    Output: list of gear indices (ndarray)
    '''

    symbols = []
    for i,l in enumerate(lines):
        for j,c in enumerate(l):
            if not c.isdigit() and c != '.':
                symbols.append(np.array([i,j]))
    return symbols


def find_adjacent_ranges(lines, symbols):
    '''Find all index ranges of parts adjacent to gear, 
    and check for pt2 validity. Will return all index ranges for 
    future parsing of numbers. Any gear that has exactly 2 parts will be 
    returned as well
    
    Input: list of input lines, list of symbol indices
    Output: List of all parts' number ranges [line_n, [start, stop]], list of valid gear indices (for part 2)
    '''

    # Check all adjacent squares
    check = np.array([
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ])
    
    ranges = []
    valid_gears = []
    for s in symbols:
        n_parts = 0
        for c in check:
            i,j = s + c
            if i >= len(lines) or i < 0 or j < 0 or j >= len(lines[i]):
                continue
            if lines[i][j].isdigit():
                # print(i)
                range = get_part_number_range(lines[i], j)            

                # If this specific number doesn't already exist in list, append
                if not [i, range] in ranges:
                    n_parts += 1
                    ranges.append([i, range])
        if n_parts == 2:
            valid_gears.append(s)
    return ranges, valid_gears

def get_part_number_range(l,j):
    ''' Find full part number range from detected digit location
    
    Input: line, index of digit
    Output: start and end indices of the part number '''

    # Forward search
    jj = j
    while True:
        jj += 1
        nend = jj-1
        if jj == len(l):
            break
        elif not l[jj].isdigit():
            break

    # Backwards Search
    for jj in range(j, -1, -1):
        nstart = jj
        if not l[jj].isdigit():
            nstart += 1
            break
    return nstart,nend
            

def part_range_to_number(lines, ranges):
    ''' Convert from part number range to integer number

    Input: input lines, list of part number ranges
    Output: list of part numbers '''

    numbers = []
    for r in ranges:
        line, (i,j) = r
        # print(r)
        numbers.append(int(lines[line][i:j+1]))
    return numbers


def calc_gear_ratios(numbers):
    ''' Calculate gear ratiios by multiplying every 2 part numbers

    Input: Valid part numbers (2 parts per gear only)
    Output: List of gear ratios'''

    if len(numbers) % 2 != 0:
        raise ValueError("Expected number of valid gears to be divisible by 2")

    ratios = []
    for i in range(0, len(numbers), 2):
        ratios.append(numbers[i]*numbers[i+1])
    return ratios


if __name__ == '__main__':
    with open(input_path) as f:
        lines = f.read().splitlines()

    # Find all symbols
    symbols = find_gears(lines)

    # Part one, all symbols.Get valid gears (2 parts exactly) for later
    ranges, valid_gears = find_adjacent_ranges(lines, symbols)
    numbers = part_range_to_number(lines, ranges)
    print(f'Part 1 sum: {sum(numbers)}')

    # Part 2
    # Get valid ranges based only on valid gears
    valid_ranges, _ = find_adjacent_ranges(lines, valid_gears)
    valid_numbers = part_range_to_number(lines, valid_ranges)
    ratios = calc_gear_ratios(valid_numbers)
    print(f'Part 2 sum of gear ratios: {sum(ratios)}')