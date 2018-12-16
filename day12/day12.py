def parse_pot(c):
    return c == '#'


def parse_initial_state(line):
    # initial_state: ...
    return list(map(parse_pot, line[15:]))


def parse_rule(line):
    # #.##. => .
    sp = line.split(' => ')
    before = tuple(map(parse_pot, sp[0]))
    after = parse_pot(sp[1])
    return (before, after)


def load_input():
    with open('input.txt') as f:
        lines = f.read().strip().splitlines()
        initial_state = parse_initial_state(lines[0])
        rules = dict(map(parse_rule, lines[2:]))
        return initial_state, rules


def get_pot_state(state, index):
    return index >= 0 and index < len(state) and state[index]


def make_next_state(state, right_index, rules):
    next_state = list(state)
    for pot_index in range(len(state)):
        rule_input = tuple(get_pot_state(state, i) for i in range(pot_index - 2, pot_index + 3))
        next_state[pot_index] = rules[rule_input]

    if next_state[0] or next_state[1]:
        next_state.insert(0, False)
        right_index += 1
    if next_state[1]:
        next_state.insert(0, False)
        right_index += 1

    if next_state[-1] or next_state[-2]:
        next_state.append(False)
    if next_state[-2]:
        next_state.append(False)

    return next_state, right_index


def calculate_pot_value(state, right_index, i):
    if not state[i]:
        return 0
    elif i < right_index:
        return i - right_index + 1
    else:
        return i - right_index


def calculate_pot_sum(state, right_index):
    return sum(calculate_pot_value(state, right_index, i) for i in range(len(state)))


def part1():
    initial_state, rules = load_input()
    state = [False, False] + initial_state + [False, False]
    right_index = 2

    for generation in range(20):
        state, right_index = make_next_state(state, right_index, rules)

    print('Part 1: {}'.format(calculate_pot_sum(state, right_index)))


def part2():
    initial_state, rules = load_input()
    state = [False, False] + initial_state + [False, False]
    right_index = 2

    generation = 0
    while True:
        generation += 1
        prev_state = state
        state, right_index = make_next_state(state, right_index, rules)
        if state[state.index(True):] == prev_state[prev_state.index(True):]:
            break

    # From this point, each generation shifts the populated pots one step to the right, based on
    # visual inspection with my input. All pots are positive at this stage. Calculate how much they
    # are worth after the remaining generations.
    remaining_generations = 50_000_000_000 - generation
    populated_pots = [calculate_pot_value(state, right_index, i) for i in range(len(state)) if state[i]]
    populated_pots_afterwards = [val + remaining_generations for val in populated_pots]

    print('Part 2: {}'.format(sum(populated_pots_afterwards)))


part1()
part2()
