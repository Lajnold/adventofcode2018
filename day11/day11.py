def get_serial():
    return 8141


def get_cell_power(serial, x, y):
    rack_id = x + 10
    power = rack_id * y
    power += serial
    power *= rack_id
    power = power // 100 % 10
    power -= 5
    return power


def get_square_power(serial, x, y, size):
    power = 0
    for xi in range(size):
        for yi in range(size):
            power += get_cell_power(serial, x + xi, y + yi)
    return power


def get_square_power_with_memoization(serial, x, y, size, cache):
    if size == 1:
        power = get_cell_power(serial, x, y)
        cache[(x, y)] = power
        return power
    else:
        power = cache[(x, y)]
        for i in range(size):
            power += get_cell_power(serial, x + size - 1, y + i)
            power += get_cell_power(serial, x + i, y + size - 1)

        cache[(x, y)] = power
        return power


def part1():
    serial = get_serial()
    max_power = None
    max_power_x = None
    max_power_y = None

    for x in range(1, 299):
        for y in range(1, 299):
            square_power = get_square_power(serial, x, y, 3)
            if max_power is None or square_power > max_power:
                max_power = square_power
                max_power_x = x
                max_power_y = y

    print('Part 1: {},{}'.format(max_power_x, max_power_y))


def part2():
    serial = get_serial()
    max_power = None
    max_power_x = None
    max_power_y = None
    max_power_size = None
    cache = {}

    for size in range(1, 301):
        for x in range(1, 301):
            for y in range(1, 301):
                power = get_square_power_with_memoization(serial, x, y, size, cache)
                if max_power is None or power > max_power:
                    max_power = power
                    max_power_x = x
                    max_power_y = y
                    max_power_size = size

    print('Part 2: {},{},{}'.format(max_power_x, max_power_y, max_power_size))


part1()
part2()
