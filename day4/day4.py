import re


with open('input.txt') as f:
    # [1518-03-06 00:02] Guard #1783 begins shift
    # [1518-07-07 00:00] falls asleep
    # [1518-06-23 00:43] wakes up
    # Sort the events chronologically.
    lines = list(sorted(f.read().strip().splitlines()))


def get_sleeping_minutes_per_guard():
    time_regex = re.compile(r'\[\d+-\d+-\d+ \d+:(\d+)\]')
    begins_regex = re.compile(r'#(\d+)')

    cur_minute = None
    asleep_minute = None
    cur_guard = None
    sleeping = {}
    for line in lines:
        cur_minute = int(time_regex.search(line).group(1))
        begins_match = begins_regex.search(line)
        if begins_match:
            cur_guard = int(begins_match.group(1))
            if not cur_guard in sleeping:
                sleeping[cur_guard] = []
        elif line.endswith('falls asleep'):
            asleep_minute = cur_minute
        else:
            # Wakes up
            for m in range(asleep_minute, cur_minute):
                sleeping[cur_guard].append(m)

    return sleeping


def get_best_minute_for_guard(sleeping, guard):
    best_times = -1
    best_minute = None
    for m in range(0, 60):
        times = sum(x == m for x in sleeping[guard])
        if times > best_times:
            best_times = times
            best_minute = m

    return best_minute, best_times


def part1():
    sleeping = get_sleeping_minutes_per_guard()
    max_sleep = -1
    max_guard = None
    for g in sleeping.keys():
        if len(sleeping[g]) > max_sleep:
            max_sleep = len(sleeping[g])
            max_guard = g

    best_minute, _ = get_best_minute_for_guard(sleeping, max_guard)
    print('Part 1: {}'.format(max_guard * best_minute))


def part2():
    sleeping = get_sleeping_minutes_per_guard()
    max_minute = -1
    max_guard = None
    max_times = -1
    for g in sleeping.keys():
        best_minute, best_times = get_best_minute_for_guard(sleeping, g)
        if best_times > max_times:
            max_times = best_times
            max_minute = best_minute
            max_guard = g

    print('Part 2: {}'.format(max_minute * max_guard))


part1()
part2()
