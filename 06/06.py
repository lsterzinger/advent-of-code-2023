f = './06-input.txt'

def parse_input(file, part2=False):
    with open(file) as f:
        time, distance = f.read().splitlines()
        time = [int(a) for a in time.split(':')[-1].split(' ') if a != '']
        distance = [int(a) for a in distance.split(':')[-1].split(' ') if a != '']

    if part2:
        time2 = ''
        for t in time:
            time2 += str(t)
        time = [int(time2)]

        distance2 = ''
        for t in distance:
            distance2 += str(t)
        distance = [int(distance2)]
    return time, distance

def loop_races(times, distances):
    num_wins = []
    for t, d in zip(times, distances):
        num_wins.append(run_race(t, d))
    return num_wins

def run_race(time, distance):
    num_wins = 0
    for t in range(time + 1):
        x = t * (time - t)
        
        win = True if (x > distance) else False
        if win: num_wins += 1
        # print(f'Hold for {t}, speed is {t} mm/s, distance is {x}. Greater than {distance}: {win}')
    return num_wins

def calc_output(num_wins):
    output = 1
    for w in num_wins:
        output *= w
    return output


times, distances = parse_input(f)

print(times, distances)
print(calc_output(loop_races(times, distances)))

times, distances = parse_input(f,part2=True)
print(times, distances)
print(calc_output(loop_races(times, distances)))

