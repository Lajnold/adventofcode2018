class Instr:
    def __init__(self, code, a, b, c):
        self.code = code
        self.a = a
        self.b = b
        self.c = c


class Sample:
    def __init__(self, before, instr, after):
        self.before = before
        self.instr = instr
        self.after = after


def parse_input(lines):
    samples = []
    program = []

    i = 0
    while i < len(lines):
        if lines[i].startswith('Before'):
            # Before: [2, 1, 0, 2]
            # 6 1 3 3
            # After:  [2, 1, 0, 0]
            before = list(map(int, lines[i][9:-1].split(', ')))
            instr_parts = list(map(int, lines[i + 1].split()))
            instr = Instr(*instr_parts)
            after = list(map(int, lines[i + 2][9:-1].split(', ')))
            samples.append(Sample(before, instr, after))
            i += 3
        elif lines[i]:
            # 15 3 1 3
            instr_parts = list(map(int, lines[i].split()))
            instr = Instr(*instr_parts)
            program.append(instr)
            i += 1
        else:
            i += 1
            
    return samples, program


def load_input():
    with open('input.txt') as f:
        lines = f.read().strip().splitlines()
        return parse_input(lines)


def addr(instr, regs):
    regs[instr.c] = regs[instr.a] + regs[instr.b]

def addi(instr, regs):
    regs[instr.c] = regs[instr.a] + instr.b

def mulr(instr, regs):
    regs[instr.c] = regs[instr.a] * regs[instr.b]

def muli(instr, regs):
    regs[instr.c] = regs[instr.a] * instr.b

def banr(instr, regs):
    regs[instr.c] = regs[instr.a] & regs[instr.b]

def bani(instr, regs):
    regs[instr.c] = regs[instr.a] & instr.b

def borr(instr, regs):
    regs[instr.c] = regs[instr.a] | regs[instr.b]

def bori(instr, regs):
    regs[instr.c] = regs[instr.a] | instr.b

def setr(instr, regs):
    regs[instr.c] = regs[instr.a]

def seti(instr, regs):
    regs[instr.c] = instr.a

def gtir(instr, regs):
    regs[instr.c] = 1 if instr.a > regs[instr.b] else 0

def gtri(instr, regs):
    regs[instr.c] = 1 if regs[instr.a] > instr.b else 0

def gtrr(instr, regs):
    regs[instr.c] = 1 if regs[instr.a] > regs[instr.b] else 0

def eqir(instr, regs):
    regs[instr.c] = 1 if instr.a == regs[instr.b] else 0

def eqri(instr, regs):
    regs[instr.c] = 1 if regs[instr.a] == instr.b else 0

def eqrr(instr, regs):
    regs[instr.c] = 1 if regs[instr.a] == regs[instr.b] else 0

ALL_OPS = [
    addr, addi,
    mulr, muli,
    banr, bani,
    borr, bori,
    setr, seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]


def part1():
    samples, program = load_input()

    num_samples_with_3plus_matches = 0

    for sample in samples:
        num_matching_ops = 0
        for op in ALL_OPS:
            sample_regs = list(sample.before)
            op(sample.instr, sample_regs)
            if sample_regs == sample.after:
                num_matching_ops += 1

        if num_matching_ops >= 3:
            num_samples_with_3plus_matches += 1

    print(f'Part 1: {num_samples_with_3plus_matches}')


def run_program(program, op_mapping):
    regs = [0, 0, 0, 0]
    for instr in program:
        op_mapping[instr.code](instr, regs)

    return regs


def figure_out_op_mapping(samples):
    candidates_per_code = dict([(code, []) for code in range(16)])
    for sample in samples:
        for op in ALL_OPS:
            sample_regs = list(sample.before)
            op(sample.instr, sample_regs)
            if sample_regs == sample.after and op not in candidates_per_code[sample.instr.code]:
                candidates_per_code[sample.instr.code].append(op)

    op_mapping = dict()
    while candidates_per_code:
        code = [pair[0] for pair in candidates_per_code.items() if len(pair[1]) == 1][0]
        op = candidates_per_code[code][0]
        op_mapping[code] = op
        del candidates_per_code[code]

        for other_pair in candidates_per_code.items():
            if op in other_pair[1]:
                other_pair[1].remove(op)

    return op_mapping


def part2():
    samples, program = load_input()

    instruction_mapping = figure_out_op_mapping(samples)
    program_regs = run_program(program, instruction_mapping)

    print(f'Part 2: {program_regs[0]}')


part1()
part2()
