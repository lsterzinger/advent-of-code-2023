import re

part2 = False
input_path = './02-input.txt'
# input_path = './02-sample.txt'

# Maxima given by puzzle
max_red, max_green, max_blue = 12, 13, 14

with open(input_path) as f:
    lines = f.read().splitlines()

def parse_game(l):

    hands = l.split(':')[1].split(';')
    nhands = len(hands)

    gamenum = int(re.findall('^Game (\d*):', l)[0])
    
    nred, ngreen, nblue = [], [], []
    for h in hands:

        parse_red = re.findall('(\d*) red', h)
        parse_green = re.findall('(\d*) green', h)
        parse_blue = re.findall('(\d*) blue', h)
    
        nred.append(int(parse_red[0]) if len(parse_red) > 0 else 0)
        ngreen.append(int(parse_green[0]) if len(parse_green) > 0 else 0)
        nblue.append(int(parse_blue[0]) if len(parse_blue) > 0 else 0)
    game =  {
        'id': gamenum,
        'nhands' : nhands,
        'maxred' : max(nred),
        'maxgreen': max(ngreen),
        'maxblue' :  max(nblue)
    }
    # print(game)
    return game

def is_possible(game):
    if game['maxred'] <= max_red and game['maxgreen'] <= max_green and game['maxblue'] <= max_blue:
        return True
    else:
        return False

def power(game):
    return game["maxred"] * game["maxblue"] * game["maxgreen"]

sum_of_possible_game_ids = 0
sum_of_powers = 0
for l in lines:

    game = parse_game(l)
    if is_possible(game):
        sum_of_possible_game_ids += game['id']

    sum_of_powers += power(game)
print('Sum of possible Game IDs:', sum_of_possible_game_ids)
print('Sum of powers:', sum_of_powers)

