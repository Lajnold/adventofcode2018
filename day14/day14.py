def get_input():
    return 890691


def digits(n):
    if n == 0:
        return [0]
    else:
        d = []
        while n > 0:
            d.append(n % 10)
            n //= 10
        return list(reversed(d))


def calculate_new_scores(scores, elf1, elf2):
    new_score = scores[elf1] + scores[elf2]
    return digits(new_score)


def advance_elf(scores, elf):
    return (elf + 1 + scores[elf]) % len(scores)


def part1():
    scores = [3, 7]
    num_recipes_before_10 = get_input()
    elf1, elf2 = 0, 1
    
    while len(scores) < num_recipes_before_10 + 10:
        scores.extend(calculate_new_scores(scores, elf1, elf2))
        elf1 = advance_elf(scores, elf1)
        elf2 = advance_elf(scores, elf2)

    next_ten = scores[num_recipes_before_10 : num_recipes_before_10+10]
    print('Part 1: {}'.format(''.join(map(str, next_ten))))


def part2():
    scores = [3, 7]
    needle = digits(get_input())
    needle_len = len(needle)
    elf1, elf2 = 0, 1

    while scores[-needle_len:] != needle and scores[-needle_len-1 : -1] != needle:
        scores.extend(calculate_new_scores(scores, elf1, elf2))
        elf1 = advance_elf(scores, elf1)
        elf2 = advance_elf(scores, elf2)

    score_string = ''.join(map(str, scores))
    needle_index = score_string.index(str(get_input()))

    print('Part 2: {}'.format(needle_index))


part1()
part2()
