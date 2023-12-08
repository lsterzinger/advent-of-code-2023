from collections import Counter

sorted_card_list = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def parse_input(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines


def split_hand_and_bet(l):

    h, b = l.split(' ')
    return h, int(b)

def rank_by_type(lines):
    bins = {
        '5': [],
        '4': [],
        'full': [],
        '3': [],
        '2pair': [],
        '1pair': [],
        'high': []
    }
    for l in lines:
        h, _ = split_hand_and_bet(l)
        count = sorted(Counter(h).values())

        if count == [5]: 
            bins['5'].append(l)
        elif count == [1,4]: 
            bins['4'].append(l)
        elif count == [2,3]:
            bins['full'].append(l)
        elif count == [1, 1, 3]:
            bins['3'].append(l)
        elif count == [1, 2, 2]:
            bins['2pair'].append(l)
        elif count == [1, 1, 1, 2]:
            bins['1pair'].append(l)
        elif count == [1, 1, 1, 1, 1]:
            bins['high'].append(l)
        else:
            raise ValueError(f'Error, no contingency for hand {h}')
    return bins

def custom_sort(hand):
    return [sorted_card_list.index(card) if (card in sorted_card_list) else 0 for card in hand]

def sorted_list(bins):
    sorted_hands = []

    for cards in bins.values():
        if len(cards) > 0:
            for c in sorted(cards, key=custom_sort, reverse=False):
                sorted_hands.append(c)

    return [[i+1, h] for i, h in enumerate(reversed(sorted_hands))]

def calc_winnings(lines):
    bins = rank_by_type(lines)
    ranks = sorted_list(bins)

    total = 0
    for (rank, line) in ranks:
        _, bet = line.split(' ')
        bet = int(bet)
        total += rank * bet
    return total
lines = parse_input('./07-input.txt')
print(calc_winnings(lines))