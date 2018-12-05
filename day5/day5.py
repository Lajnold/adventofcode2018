with open('input.txt') as f:
    units = list(f.read().strip())


def reduce_polymers(polymer):
    i = 0
    reduced = list(polymer)
    while i < len(reduced) - 1:
        if reduced[i] != reduced[i + 1] and reduced[i].upper() == reduced[i + 1].upper():
            del reduced[i]
            del reduced[i]
            i -= 1
        else:
            i += 1

    return reduced


def part1():
    print('Part 1: {}'.format(len(reduce_polymers(units))))


def part2():
    unique_types = set(x.upper() for x in units)
    shortest = len(units)
    for t in unique_types:
        units_without_type = [x for x in units if x.upper() != t]
        reduced = reduce_polymers(units_without_type)
        if len(reduced) < shortest:
            shortest = len(reduced)

    print('Part 2: {}'.format(shortest))


part1()
part2()
