import re

input_file = './04-input.txt'

def parse_input(filename):
    ''' Parse input file, returning list of [card number, winning number (list), my numbers (list)] '''
    with open(filename) as f:
        lines = f.read().splitlines()

    cards = []
    for l in lines:
        cardnum = int(re.findall('^Card *(\d*):', l)[0])

        win_nums = [int(a) for a in re.findall(':(.*)\|', l)[0].split(' ') if a != '']
        my_nums = [int(a) for a in re.findall('\|(.*)$', l)[0].split(' ') if a != '']

        cards.append([cardnum, win_nums, my_nums])
    
    return cards


def get_points(card):
    ''' Get the total points (2^(counter-1)) of a card''' 
    cardnum, win_nums, my_nums = card

    counter = 0
    for c in my_nums:
        if c in win_nums: counter += 1
    
    return 2**(counter-1) if counter >0 else 0


def points_in_deck(deck):
    ''' Sum up all the points for each card in the deck'''
    total = 0
    for card in deck:
        total += get_points(card)
    return total


def num_new_cards(card):
    ''' Return integer of how many new cards granted by current card (pt2)'''
    cardnum, win_nums, my_nums = card

    newcards = []
    for c in my_nums:
        if c in win_nums: newcards.append(c)
    return len(newcards)


def copies_of_each_card(deck):
    ''' Build array of how many copies of each number are given at the end'''
    number = [1 for i in range(len(deck))]
    for i in range(len(deck)):
        new_cards = num_new_cards(deck[i])
        for j in range(1, new_cards+1):
            number[i+j] += number[i]
    return number

if __name__ == '__main__':
    deck = parse_input(input_file)
    print('Part 1: Total Points in Deck:', points_in_deck(deck))
    print('Part 2: Total Number of Cards', sum(copies_of_each_card(deck)))