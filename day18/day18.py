OPEN = '.'
TREES = '|'
LUMBERYARD = '#'


def load_input():
    with open('input.txt') as f:
        return [list(line) for line in f.read().rstrip().splitlines()]


def count_adjacent(state, x, y, type):
    count = 0
    for y2 in range(y-1, y+2):
        for x2 in range(x-1, x+2):
            within_bounds = y2 >= 0 and y2 < len(state) and x2 >= 0 and x2 < len(state[y2])
            if (x != x2 or y != y2) and within_bounds and state[y2][x2] == type:
                count += 1

    return count


def next_state(state):
    new_state = []
    for y in range(len(state)):
        new_line = []
        for x in range(len(state[y])):
            old_type = state[y][x]
            new_type = old_type
            if old_type == OPEN:
                trees = count_adjacent(state, x, y, TREES)
                if trees >= 3:
                    new_type = TREES
            elif old_type == TREES:
                lumberyards = count_adjacent(state, x, y, LUMBERYARD)
                if lumberyards >= 3:
                    new_type = LUMBERYARD
            else:
                trees = count_adjacent(state, x, y, TREES)
                lumberyards = count_adjacent(state, x, y, LUMBERYARD)
                if trees == 0 or lumberyards == 0:
                    new_type = OPEN

            new_line.append(new_type)
            
        new_state.append(new_line)

    return new_state


def resource_value(state):
    trees = sum(
        1
        for line in state
        for c in line
        if c == TREES)

    lumberyards = sum(
        1
        for line in state
        for c in line
        if c == LUMBERYARD)

    return trees * lumberyards


def string_state(state):
    s = ''
    for y in range(len(state)):
        for x in range(len(state[y])):
            s += state[y][x]
        if y < len(state) - 1:
            s += '\n'
    return s


def part1():
    state = load_input()
    for _ in range(10):
        state = next_state(state)
        
    print(f'Part 1: {resource_value(state)}')


def part2():
    initial_state = load_input()

    state = initial_state
    state_list = [initial_state]
    state_set = set()
    state_set.add(string_state(initial_state))
    while True:
        state = next_state(state)
        new_string_state = string_state(state)
        if new_string_state in state_set:
            break
        else:
            state_list.append(state)
            state_set.add(new_string_state)

    minutes_passed = len(state_list)
    minutes_left = 1_000_000_000 - minutes_passed

    first_state_in_cycle = state
    first_state_in_cycle_string = string_state(first_state_in_cycle)
    cycle_start_index = len(state_list) - 1
    while True:
        if string_state(state_list[cycle_start_index]) == first_state_in_cycle_string:
            break
        else:
            cycle_start_index -= 1

    num_states_in_cycle = len(state_list) - cycle_start_index
    final_index = cycle_start_index + (minutes_left % num_states_in_cycle)
    final_state = state_list[final_index]

    print(f'Part 2: {resource_value(final_state)}')


part1()
part2()
