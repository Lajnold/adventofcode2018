import re


class Claim:
    # #1 @ 817,273: 26x26
    claim_regex = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

    def __init__(self, line):
        m = Claim.claim_regex.match(line)
        self.id = int(m.group(1))
        self.x = int(m.group(2))
        self.y = int(m.group(3))
        self.w = int(m.group(4))
        self.h = int(m.group(5))


with open('input.txt') as f:
    lines = f.read().strip().splitlines()
    claims = list(map(Claim, lines))


def square_count():
    counts = [0] * 1000 * 1000
    for claim in claims:
        for y in range(claim.y, claim.y + claim.h):
            for x in range(claim.x, claim.x + claim.w):
                counts[y * 1000 + x] += 1

    return counts


def part1():
    counts = square_count()
    num_overlapping = sum(n > 1 for n in counts)
    print('Part 1: {}'.format(num_overlapping))


def get_nonoverlapping_id():
    counts = square_count()
    for claim in claims:
        overlaps = False
        for y in range(claim.y, claim.y + claim.h):
            for x in range(claim.x, claim.x + claim.w):
                if counts[y * 1000 + x] > 1:
                    overlaps = True

        if not overlaps:
            return claim.id


def part2():
   print('Part 2: {}'.format(get_nonoverlapping_id()))


part1()
part2()
