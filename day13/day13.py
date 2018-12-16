class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.next_turn = 'l'

    def move(self):
        if self.direction == '<':
            self.x -= 1
        elif self.direction == '>':
            self.x += 1
        elif self.direction == '^':
            self.y -= 1
        else:
            self.y += 1

    def maybe_turn(self, track):
        if track in ['\\', '/']:
            self.turn_at_curve(track)
        elif track == '+':
            self.turn_at_intersection()

    def turn_at_curve(self, curve):
        if self.direction == '<':
            if curve == '\\':
                self.direction = '^'
            elif curve == '/':
                self.direction = 'v'
        elif self.direction == '>':
            if curve == '\\':
                self.direction = 'v'
            else:
                self.direction = '^'
        elif self.direction == '^':
            if curve == '\\':
                self.direction = '<'
            else:
                self.direction = '>'
        elif self.direction == 'v':
            if curve == '\\':
                self.direction = '>'
            else:
                self.direction = '<'

    def turn_at_intersection(self):
        if self.direction == '<':
            if self.next_turn == 'l':
                self.direction = 'v'
            elif self.next_turn == 'r':
                self.direction = '^'
        elif self.direction == '>':
            if self.next_turn == 'l':
                self.direction = '^'
            elif self.next_turn == 'r':
                self.direction = 'v'
        elif self.direction == '^':
            if self.next_turn == 'l':
                self.direction = '<'
            elif self.next_turn == 'r':
                self.direction = '>'
        elif self.direction == 'v':
            if self.next_turn == 'l':
                self.direction = '>'
            elif self.next_turn == 'r':
                self.direction = '<'
        
        if self.next_turn == 'l':
            self.next_turn = 's'
        elif self.next_turn == 's':
            self.next_turn = 'r'
        else:
            self.next_turn = 'l'


def replace_carts_with_track(lines):
    return [line.replace('<', '-').replace('>', '-').replace('^', '|').replace('v', '|') for line in lines]


def make_carts(lines):
    carts = []
    for y in range(len(lines)):
        line = lines[y]
        for x in range(len(line)):
            if line[x] in ['<', '>', '^', 'v']:
                carts.append(Cart(x, y, line[x]))

    return carts


def load_input():
    with open('input.txt') as f:
        lines = f.read().rstrip().splitlines()
        tracks = replace_carts_with_track(lines)
        carts = make_carts(lines)
        return tracks, carts


def check_collision(carts, moved_cart):
    for cart in carts:
        if cart is not moved_cart \
                and cart.x == moved_cart.x \
                and cart.y == moved_cart.y:
            return cart

    return None


def part1():
    tracks, carts = load_input()
    
    collided_cart = None
    while collided_cart is None:
        for cart in sorted(carts, key=lambda c: (c.y, c.x)):
            cart.move()
            collided_cart = check_collision(carts, cart)
            if collided_cart:
                break
            cart.maybe_turn(tracks[cart.y][cart.x])

    print('Part 1: {},{}'.format(collided_cart.x, collided_cart.y))


def part2():
    tracks, carts = load_input()
    
    while len(carts) > 1:
        for cart in sorted(carts, key=lambda c: (c.y, c.x)):
            if cart not in carts:
                # Was broken by another cart.
                continue

            cart.move()
            
            collided_cart = check_collision(carts, cart)
            if collided_cart:
                carts.remove(cart)
                carts.remove(collided_cart)
            else:
                cart.maybe_turn(tracks[cart.y][cart.x])

    print('Part 2: {},{}'.format(carts[0].x, carts[0].y))


part1()
part2()
