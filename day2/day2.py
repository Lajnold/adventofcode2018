with open('input.txt') as f:
    lines = f.readlines()


def char_counts(line):
    counts = dict()
    for c in line:
        counts[c] = counts.get(c, 0) + 1
    return counts
    
def part1():
    twos = 0
    threes = 0
    for line in lines:
        counts = char_counts(line)
        if 2 in counts.values():
            twos += 1
        if 3 in counts.values():
            threes += 1

    print('Part 1: {}'.format(twos * threes))


def find_diffs(a, b):
    diffs = 0
    d = None
    for i in range(len(a)):
        if a[i] != b[i]:
            diffs += 1
            d = i

    # Number of diffs and index of last diff
    return diffs, d

def find_common_letters():
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            diffs, d = find_diffs(lines[i], lines[j])
            if diffs == 1:
                return lines[i][:d] + lines[i][d+1:]

def part2():
    print('Part 2: {}'.format(find_common_letters()))


part1()
part2()
