part2 = True

numbers = {
    'one' : 1,
    'two' : 2,
    'three' : 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
}

with open('./01-sample.txt') as input:
    total = 0
    for l in input.readlines():
        if part2:
            # If doing part to, replace the words of digits with the digits themselves
            l2 = l
            for t,i in numbers.items():
                l = l.replace(t, str(i))
            print(l, l2)
        digits = [s for s in l if s.isdigit()]
        
        number = int(digits[0] + digits[-1])
        total += number
    print(total)