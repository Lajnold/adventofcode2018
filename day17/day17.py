class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        return Pos(self.x, self.y - 1)

    def down(self):
        return Pos(self.x, self.y + 1)

    def left(self):
        return Pos(self.x - 1, self.y)

    def right(self):
        return Pos(self.x + 1, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'Pos({self.x}, {self.y})'

    def __repr__(self):
        return str(self)


def parse_range(r):
    # 533
    # 456..458
    sp = r.split('..')
    if len(sp) == 1:
        return [int(sp[0])]
    else:
        return list(range(int(sp[0]), int(sp[1]) + 1))


def parse_input(lines):
    clays = []
    for line in lines:
        # x=533, y=1429..1441
        # y=1785, x=456..458
        sp = line.split(', ')
        x_part = sp[0][2:] if sp[0][0] == 'x' else sp[1][2:]
        y_part = sp[0][2:] if sp[0][0] == 'y' else sp[1][2:]
        for x in parse_range(x_part):
            for y in parse_range(y_part):
                clays.append(Pos(x, y))
    
    return clays


def load_input():
    with open('input.txt') as f:
        lines = f.read().strip().splitlines()
        return parse_input(lines)


def write_map_to_file(clay, water):
    min_x = min(clay.x for clay in clay)
    max_x = max(clay.x for clay in clay)
    min_y = min(clay.y for clay in clay)
    max_y = max(clay.y for clay in clay)

    with open('output.txt', 'w') as f:
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                here = Pos(x, y)
                if here in clay:
                    f.write('#')
                elif here in water:
                    f.write('~')
                else:
                    f.write('.')

            f.write('\n')


def part1():
    clay = set(load_input())
    min_y = min(clay.y for clay in clay)
    max_y = max(clay.y for clay in clay)

    sources = [Pos(500, 0)]
    water = set()

    while sources:
        source = sources[0]
        del sources[0]

        expander = None
        source = source.down()
        while source and source.y <= max_y:
            if source in clay:
                expander = source.up()
                source = None
            elif source in water:
                expander = source
                source = None
            else:
                if source.y >= min_y:
                    water.add(source)
                source = source.down()

        while expander:
            left_clay = False
            left_expander = expander.left()
            while left_expander:
                if left_expander in clay:
                    left_clay = True
                    left_expander = None
                else:
                    if left_expander.down() in clay or left_expander.down() in water:
                        if left_expander.y >= min_y:
                            water.add(left_expander)
                        left_expander = left_expander.left()
                    else:
                        if left_expander.right().down() in clay:
                            sources.append(left_expander.up())
                        left_expander = None

            right_clay = False
            right_expander = expander.right()
            while right_expander:
                if right_expander in clay:
                    right_clay = True
                    right_expander = None
                else:
                    if right_expander.down() in clay or right_expander.down() in water:
                        if right_expander.y >= min_y:
                            water.add(right_expander)
                        right_expander = right_expander.right()
                    else:
                        if right_expander.left().down() in clay:
                            sources.append(right_expander.up())
                        right_expander = None

            if left_clay and right_clay:
                expander = expander.up()
                if expander.y >= min_y:
                    water.add(expander)
            else:
                expander = None

    write_map_to_file(clay, water)
    print(f'Part 1: {len(water)}')


def part2():
    pass


part1()
part2()
