class Unit:
    def __init__(self, race, x, y, attack_power):
        self.race = race
        self.x = x
        self.y = y
        self.attack_power = attack_power
        self.hp = 200

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Unit({self.race}, {self.x}, {self.y}, {self.hp}, {self.attack_power})"


def parse_map(lines):
    units = []
    tiles = []
    for y in range(len(lines)):
        line = lines[y]
        tiles.append([])
        for x in range(len(line)):
            c = line[x]
            tiles[y].append('#' if c == '#' else '.')
            if c == 'E' or c == 'G':
                units.append(Unit(c, x, y, 3))

    return tiles, units


def load_input():
    with open('input.txt') as f:
        lines = f.read().strip().splitlines()
        return parse_map(lines)


def reading_order(units):
    return sorted(units, key=lambda u: u.y * 1000 + u.x)


def is_enemy(unit, target):
    return unit.race != target.race


def get_enemy_list(unit, units):
    return [u for u in units if is_enemy(unit, u)]


def is_adjacent(unit, target):
    return (unit.x == target.x and abs(unit.y - target.y) == 1) \
        or (unit.y == target.y and abs(unit.x - target.x) == 1)


def select_adjacent_enemy_to_attack(unit, units):
    adjacents = [e for e in units if is_enemy(unit, e) and is_adjacent(unit, e)]
    if adjacents:
        least_hp = min(u.hp for u in adjacents)
        enemies_with_least_hp = [e for e in adjacents if e.hp == least_hp]
        return reading_order(enemies_with_least_hp)[0]
    else:
        return None


def find_path_to_move(unit, units, tiles):
    locations = [
        (unit.x, unit.y - 1, []),
        (unit.x - 1, unit.y, []),
        (unit.x + 1, unit.y, []),
        (unit.x, unit.y + 1, [])
    ]
    visited_locations = set()
    visited_locations.add((unit.x, unit.y))

    found_path = None
    while locations and not found_path:
        loc = locations[0]
        del locations[0]
        if (loc[0], loc[1]) in visited_locations:
            continue
        if tiles[loc[1]][loc[0]] == '#':
            continue

        visited_locations.add((loc[0], loc[1]))
        units_here = [e for e in units if e.x == loc[0] and e.y == loc[1]]

        if units_here:
            if is_enemy(unit, units_here[0]):
                found_path = loc[2]
        else:
            locations.append((loc[0], loc[1] - 1, loc[2] + [(loc[0], loc[1])]))
            locations.append((loc[0] - 1, loc[1], loc[2] + [(loc[0], loc[1])]))
            locations.append((loc[0] + 1, loc[1], loc[2] + [(loc[0], loc[1])]))
            locations.append((loc[0], loc[1] + 1, loc[2] + [(loc[0], loc[1])]))

    return found_path


def move(unit, path):
    unit.x = path[0][0]
    unit.y = path[0][1]


def attack(unit, target, units):
    target.hp -= unit.attack_power
    if target.hp <= 0:
        units.remove(target)


def both_races_left(units):
    return any(u.race == 'E' for u in units) \
        and any(u.race == 'G' for u in units)


def run_simulation(tiles, units):
    full_rounds = 0

    while both_races_left(units):
        for unit in reading_order(units):
            if unit.hp > 0:
                enemy_before_move = select_adjacent_enemy_to_attack(unit, units)
                if enemy_before_move:
                    attack(unit, enemy_before_move, units)
                else:
                    path = find_path_to_move(unit, units, tiles)
                    if path:
                        move(unit, path)

                        enemy_after_move = select_adjacent_enemy_to_attack(unit, units)
                        if enemy_after_move:
                            attack(unit, enemy_after_move, units)

        if both_races_left(units):
            full_rounds += 1
        
    return units, full_rounds


def part1():
    tiles, units = load_input()

    units_left, full_rounds = run_simulation(tiles, units)

    hp_left = sum(u.hp for u in units_left)
    print(f'Part 1: {full_rounds * hp_left}')


def part2():
    tiles, units = load_input()
    num_elves = len([u for u in units if u.race == 'E'])
    attack_power = 4
    while True:
        goblins = [Unit(u.race, u.x, u.y, u.attack_power) for u in units if u.race == 'G']
        elves = [Unit(u.race, u.x, u.y, attack_power) for u in units if u.race == 'E']
        units_left, full_rounds = run_simulation(tiles, goblins + elves)
        if units_left[0].race == 'E' and len(units_left) == num_elves:
            break
        attack_power += 1

    hp_left = sum(u.hp for u in units_left)
    print(f'Part 2: {full_rounds * hp_left}')


part1()
part2()
