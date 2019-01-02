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


class Node:
    def __init__(self, pos):
        self.pos = pos
        self.connections = set()


def load_input():
    with open('input.txt') as f:
        return f.read().rstrip()


def next_pos_from_char(pos, c):
    if c == 'N':
        return pos.up()
    elif c == 'S':
        return pos.down()
    elif c == 'W':
        return pos.left()
    elif c == 'E':
        return pos.right()


def parse_sub_graph(regex, regex_idx, nodes, prev_pos):
    # ^ENWWW(NEEE|SSE(EE|N))EEEN$

    current_positions = set([prev_pos])
    return_positions = set()

    while regex_idx < len(regex):
        c = regex[regex_idx]

        if c == '^':
            regex_idx += 1

        elif c in ('N', 'S', 'W', 'E'):
            next_positions = set()
            for pos in current_positions:
                node = nodes[pos]
                next_pos = next_pos_from_char(node.pos, c)

                next_node = nodes.get(next_pos)
                if not next_node:
                    next_node = Node(next_pos)
                    nodes[next_pos] = next_node

                node.connections.add(next_node)
                next_node.connections.add(node)

                next_positions.add(next_pos)
                
            current_positions = next_positions
            regex_idx += 1

        elif c == '(':
            next_positions = set()
            for pos in current_positions:
                # The new regex_idx will be the same for all sub calls, so just remember the last one.
                regex_idx, sub_positions = parse_sub_graph(regex, regex_idx + 1, nodes, pos)
                next_positions.update(sub_positions)
            current_positions = next_positions

        elif c == '|':
            return_positions.update(current_positions)
            current_positions = [prev_pos]
            regex_idx += 1

        elif c == ')':
            return_positions.update(current_positions)
            return regex_idx + 1, return_positions

        elif c == '$':
            return regex_idx + 1, []


def build_graph(regex):
    node = Node(Pos(0, 0))
    nodes = { node.pos: node }
    parse_sub_graph(regex, 0, nodes, node.pos)
    return nodes


def save_map(nodes):
    positions = nodes.keys()
    min_x = min(p.x for p in positions)
    max_x = max(p.x for p in positions)
    min_y = min(p.y for p in positions)
    max_y = max(p.y for p in positions)
    
    rooms_x = max_x - min_x + 1
    rooms_y = max_y - min_y + 1

    m = ('#' * (rooms_x * 2 + 1)) + '\n'

    for y in range(rooms_y * 2 - 1):
        m += '#'
        room_y = y // 2 + min_y
        for x in range(rooms_x * 2 - 1):
            room_x = x // 2 + min_x
            pos = Pos(room_x, room_y)
            if y % 2 == 0 and x % 2 == 0:
                if pos == Pos(0, 0):
                    m += 'X'
                elif pos in nodes:
                    m += '.'
                else:
                    m += '#'
            elif y % 2 == 0:
                left = nodes.get(pos)
                right = nodes.get(pos.right())
                if left and right and left in right.connections:
                    m += '|'
                else:
                    m += '#'
            elif x % 2 == 0:
                up = nodes.get(pos)
                down = nodes.get(pos.down())
                if up and down and up in down.connections:
                    m += '-'
                else:
                    m += '#'
            else:
                m += '#'
        m += '#' + '\n'

    m += ('#' * (rooms_x * 2 + 1)) + '\n'

    with open('map.txt', 'w') as f:
        f.write(m)


def find_distances(nodes):
    pending = [(nodes[Pos(0, 0)], 0)]
    distances = { Pos(0, 0): 0 }
    while pending:
        node, dist = pending[0]
        distances[node.pos] = dist
        del pending[0]
        
        unvisited = (conn for conn in node.connections if conn.pos not in distances)
        pending.extend(((conn, dist + 1) for conn in unvisited))

    return distances


def main():
    regex = load_input()
    # regex = '^ENWWW(NEEE|SSE(EE|N))$'
    # regex = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'
    nodes = build_graph(regex)
    # save_map(nodes)

    distances = find_distances(nodes)
    max_distance = max(distances.values())
    num_far_away = sum(1 for d in distances.values() if d >= 1000)

    print(f'Part 1: {max_distance}')
    print(f'Part 2: {num_far_away}')


main()
