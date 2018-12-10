class Worker:
    def __init__(self, step, started_when):
        self.step = step
        self.started_when = started_when


def load_input_file():
    with open('input.txt') as f:
        return f.read().strip().splitlines()


def parse_dependencies(lines):
    dependencies = {}
    for line in lines:
        before, after = line[5], line[36]
        if after in dependencies:
            dependencies[after].append(before)
        else:
            dependencies[after] = [before]

    return dependencies


def part1():
    input_lines = load_input_file()
    dependencies = parse_dependencies(input_lines)

    remaining_steps = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    completed_steps = []
    while remaining_steps:
        for step in remaining_steps:
            deps = dependencies.get(step, [])
            if all(d in completed_steps for d in deps):
                completed_steps.append(step)
                remaining_steps.remove(step)
                break

    print('Part 1: {}'.format(''.join(completed_steps)))


def part2():
    input_lines = load_input_file()
    dependencies = parse_dependencies(input_lines)

    workers = []
    remaining_steps = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    completed_steps = []
    started_steps = []
    current_sec = 0

    while remaining_steps:
        completed_workers = [w for w in workers if w.started_when + 60 + ord(w.step) - 64 == current_sec]
        for w in completed_workers:
            completed_steps.append(w.step)
            remaining_steps.remove(w.step)
            workers.remove(w)

        for step in remaining_steps:
            deps = dependencies.get(step, [])
            if len(workers) < 5 and step not in started_steps and all(d in completed_steps for d in deps):
                workers.append(Worker(step, current_sec))
                started_steps.append(step)

        current_sec += 1

    # The loop ticked one second after everything was completed.
    finished_sec = current_sec - 1

    print('Part 2: {}'.format(finished_sec))
    


part1()
part2()
