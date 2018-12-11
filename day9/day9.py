def load_game_def():
    with open('input.txt') as f:
        # 416 players; last marble is worth 71617 points
        words = f.read().strip().split()
        num_players = int(words[0])
        last_marble = int(words[6])
        return num_players, last_marble


def run_game(num_players, last_marble):
    scores = [0 for n in range(num_players)]
    marbles = [0]
    cur_player = 0
    cur_marble = 1
    cur_position = 0
    while cur_marble <= last_marble:
        if cur_marble % 23 == 0:
            scores[cur_player] += cur_marble
            cur_position = (cur_position - 7) % len(marbles)
            scores[cur_player] += marbles[cur_position]
            del marbles[cur_position]
            if cur_position == len(marbles):
                cur_position = 0
        else:
            if len(marbles) == 1:
                cur_position = 1
            else:
                cur_position = (cur_position + 2) % len(marbles)

            marbles.insert(cur_position, cur_marble)

        cur_player = (cur_player + 1) % num_players
        cur_marble += 1

    return scores


def part1():
    num_players, last_marble = load_game_def()
    scores = run_game(num_players, last_marble)
    print('Part 1: {}'.format(max(scores)))


def part2():
    print('Not running part 2; the array-based Python implementation is too slow')
    # num_players, last_marble = load_game_def()
    # last_marble *= 100
    # scores = run_game(num_players, last_marble)
    # print('Part 2: {}'.format(max(scores)))


part1()
part2()
