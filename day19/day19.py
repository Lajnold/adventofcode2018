def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]

def addi(regs, a, b, c):
    regs[c] = regs[a] + b

def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]

def muli(regs, a, b, c):
    regs[c] = regs[a] * b

def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]

def bani(regs, a, b, c):
    regs[c] = regs[a] & b

def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]

def bori(regs, a, b, c):
    regs[c] = regs[a] | b

def setr(regs, a, b, c):
    regs[c] = regs[a]

def seti(regs, a, b, c):
    regs[c] = a

def gtir(regs, a, b, c):
    regs[c] = 1 if a > regs[b] else 0

def gtri(regs, a, b, c):
    regs[c] = 1 if regs[a] > b else 0

def gtrr(regs, a, b, c):
    regs[c] = 1 if regs[a] > regs[b] else 0

def eqir(regs, a, b, c):
    regs[c] = 1 if a == regs[b] else 0

def eqri(regs, a, b, c):
    regs[c] = 1 if regs[a] == b else 0

def eqrr(regs, a, b, c):
    regs[c] = 1 if regs[a] == regs[b] else 0


INSTRS = {
    'addr': addr, 'addi': addi,
    'mulr': mulr, 'muli': muli,
    'banr': banr, 'bani': bani,
    'borr': borr, 'bori': bori,
    'setr': setr, 'seti': seti,
    'gtir': gtir, 'gtri': gtri, 'gtrr': gtrr,
    'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr
}


class Instr:
    def __init__(self, mnemonic, a, b, c):
        self.mnemonic = mnemonic
        self.impl = INSTRS[mnemonic]
        self.a = a
        self.b = b
        self.c = c

    def exec(self, regs):
        INSTRS[self.mnemonic](regs, self.a, self.b, self.c)

    def __str__(self):
        return f'Instr({self.mnemonic} {self.a} {self.b} {self.c})'

    def __repr__(self):
        return str(self)


class Program:
    def __init__(self, instructions, ip_reg):
        self.instructions = instructions
        self.ip_reg = ip_reg
        self.ip = 0
        self.regs = [0 for _ in range(6)]

    def is_valid_ip(self):
        return 0 <= self.ip < len(self.instructions)

    def exec(self):
        instr = self.instructions[self.ip]
        self.regs[self.ip_reg] = self.ip
        instr.exec(self.regs)
        self.ip = self.regs[self.ip_reg]
        self.ip += 1


def parse_input(lines):
    ip_reg = int(lines[0].split()[-1])

    instructions = []
    for line in lines[1:]:
        mnemonic, a, b, c = line.split()
        instructions.append(Instr(mnemonic, int(a), int(b), int(c)))

    return Program(instructions, ip_reg)


def load_program():
    with open('input.txt') as f:
        lines = f.read().rstrip().splitlines()
        return parse_input(lines)


def sum_of_divisors(n):
    # The input program calculates the sum of all divisors of a number. For part 1, that number is
    # 974, which is quick. For part 2, the number is 10551374, which takes too long. This is a more
    # efficient way of calculating the sum of the divisors.

    # The number is a divisor of itself, and can also be divided by numbers up to half the size.
    return n + sum(i for i in range(1, n // 2 + 1) if n % i == 0)


def part1():
    prog = load_program()
    while prog.is_valid_ip():
        prog.exec()

    print(f'Part 1: {prog.regs[0]}')


def part2():
    prog = load_program()
    prog.regs[0] = 1

    # The target number is in r3 once the looping starts, which it does when ip == 3.
    while prog.is_valid_ip() and prog.ip != 3:
        prog.exec()
    target = prog.regs[3]

    print(f'Part 2: {sum_of_divisors(target)}')


part1()
part2()
