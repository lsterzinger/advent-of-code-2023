part2 = False
input_path = './01-input.txt'

# Translation dictionary of natural language numbers to string digit
number_dict = {
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
}


# Start at the left, return if digit
def find_left_number(l, part2=False):
    i = 0
    while i < len(l):
        if l[i].isdigit(): 
            return l[i]

        # If doing part to, return digit if first `i` characters 
        # match a natural language number
        elif part2:
            for n in number_dict.keys():
                if n in l[:i+1]:
                    return number_dict[n]
        i += 1 
    return None

# Start at right, return if digit
def find_right_number(l, part2=False):
    i = len(l)-1
    while i >= 0:
        if l[i].isdigit(): return l[i]
        
        # If doing part 2, return digit if characters from i -> end 
        # match a natural language number
        elif part2:
            for n in number_dict.keys():
                if n in l[i:]:
                    return number_dict[n]
        i -= 1
    return None

with open(input_path) as f:
    lines = f.read().splitlines()

total = 0
for l in lines:
    d1 = find_left_number(l, part2)
    d2 = find_right_number(l, part2)

    number = int(d1 + d2)
    total += number
print(total)