with open('input.txt') as f:
    nums = list(map(int, f.readlines()))


def part1():
    print('Part 1: {}'.format(sum(nums)))


def part2():
    def find():
        freq = 0
        freqs = set()
        while True:
            for n in nums:
                freq += n
                if freq in freqs:
                    return freq
                freqs.add(freq)

    print('Part 2: {}'.format(find()))


part1()
part2()
