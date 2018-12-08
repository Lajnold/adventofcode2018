class Pos:
    def __init__(self, definition):
        sp = definition.split(', ')
        self.x = int(sp[0])
        self.y = int(sp[1])

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)


with open('input.txt') as f:
    lines = f.read().strip().splitlines()
    destinations = list(map(Pos, lines))


def manhattan(dest, x, y):
    return abs(dest.x - x) + abs(dest.y - y)


def closest_destination(x, y):
    distances = ((d, manhattan(d, x, y)) for d in destinations)
    sorted_distances = sorted(distances, key=lambda x: x[1])
    if sorted_distances[0][1] == sorted_distances[1][1]:
        return None
    else:
        return sorted_distances[0][0]


def find_largest_area():
    min_x = min(dest.x for dest in destinations)
    min_y = min(dest.y for dest in destinations)
    max_x = max(dest.x for dest in destinations)
    max_y = max(dest.y for dest in destinations)

    closest_count = {}
    infinite_destinations = set()
    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            closest_dest = closest_destination(x, y)
            if closest_dest is not None:
                closest_count[closest_dest] = closest_count.get(closest_dest, 0) + 1

                if x in (min_x, max_x) or y in (min_y, max_y):
                    infinite_destinations.add(closest_dest)

    for count_item in sorted(closest_count.items(), key=lambda x: x[1], reverse=True):
        dest, area = count_item
        if dest not in infinite_destinations:
            return area


def find_size_of_close_region():
    min_x = min(dest.x for dest in destinations)
    min_y = min(dest.y for dest in destinations)
    max_x = max(dest.x for dest in destinations)
    max_y = max(dest.y for dest in destinations)

    num_close = 0
    for x in range(min_x - 9999, max_x + 9999 + 1):
        for y in range(min_y - 9999, max_y + 9999 + 1):
            print('x: {}, y: {}'.format(x, y))
            dist_sum = 0
            for dest in destinations:
                dist_sum += manhattan(dest, x, y)

            if dist_sum < 10000:
                num_close += 1

    return num_close


def part1():
    print('Part 1: {}'.format(find_largest_area()))


def part2():
    print('Part 2: {}'.format(find_size_of_close_region()))


part1()
part2()
