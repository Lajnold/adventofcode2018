#include <stdio.h>
#include <stdlib.h>

typedef unsigned long long reg_t;

reg_t run(reg_t initial_r0)
{
    reg_t r[6] = { initial_r0, 0, 0, 0, 0, 0 };
    reg_t ip = 0;

    goto first;

next:
    ip = r[2];
    ip++;
    if (ip > 35) {
        return r[0];
    }
first:
    r[2] = ip;
    // printf("ip: %llu, r0: %llu, r1: %llu, r2: %llu, r3: %llu, r4: %llu, r5: %llu\n", ip, r[0], r[1], r[2], r[3], r[4], r[5]);
    switch (ip) {
        case 0:  // addi 2 16 2
            r[2] = r[2] + 16;
            goto next;
        case 1:  // seti 1 0 4
            r[4] = 1;
            goto next;
        case 2:  // seti 1 5 5
            r[5] = 1;
            goto next;
        case 3:  // mulr 4 5 1
            r[1] = r[4] * r[5];
            goto next;
        case 4:  // eqrr 1 3 1
            r[1] = (r[1] == r[3]);
            goto next;
        case 5:  // addr 1 2 2
            r[2] = r[1] + r[2];
            goto next;
        case 6:  // addi 2 1 2
            r[2] = r[2] + 1;
            goto next;
        case 7:  // addr 4 0 0
            r[0] = r[4] + r[0];
            goto next;
        case 8:  // addi 5 1 5
            r[5] = r[5] + 1;
            goto next;
        case 9:  // gtrr 5 3 1
            r[1] = (r[5] > r[3]);
            goto next;
        case 10:  // addr 2 1 2
            r[2] = r[2] + r[1];
            goto next;
        case 11:  // seti 2 6 2
            r[2] = 2;
            goto next;
        case 12:  // addi 4 1 4
            r[4] = r[4] + 1;
            goto next;
        case 13:  // gtrr 4 3 1
            r[1] = (r[4] > r[3]);
            goto next;
        case 14:  // addr 1 2 2
            r[2] = r[1] + r[2];
            goto next;
        case 15:  // seti 1 7 2
            r[2] = 1;
            goto next;
        case 16:  // mulr 2 2 2
            r[2] = r[2] * r[2];
            goto next;
        case 17:  // addi 3 2 3
            r[3] = r[3] + 2;
            goto next;
        case 18:  // mulr 3 3 3
            r[3] = r[3] * r[3];
            goto next;
        case 19:  // mulr 2 3 3
            r[3] = r[2] * r[3];
            goto next;
        case 20:  // muli 3 11 3
            r[3] = r[3] * 11;
            goto next;
        case 21:  // addi 1 6 1
            r[1] = r[1] + 6;
            goto next;
        case 22:  // mulr 1 2 1
            r[1] = r[1] * r[2];
            goto next;
        case 23:  // addi 1 6 1
            r[1] = r[1] + 6;
            goto next;
        case 24:  // addr 3 1 3
            r[3] = r[3] + r[1];
            goto next;
        case 25:  // addr 2 0 2
            r[2] = r[2] + r[0];
            goto next;
        case 26:  // seti 0 3 2
            r[2] = 0;
            goto next;
        case 27:  // setr 2 3 1
            r[1] = r[2];
            goto next;
        case 28:  // mulr 1 2 1
            r[1] = r[1] * r[2];
            goto next;
        case 29:  // addr 2 1 1
            r[1] = r[2] + r[1];
            goto next;
        case 30:  // mulr 2 1 1
            r[1] = r[2] * r[1];
            goto next;
        case 31:  // muli 1 14 1
            r[1] = r[1] * 14;
            goto next;
        case 32:  // mulr 1 2 1
            r[1] = r[1] * r[2];
            goto next;
        case 33:  // addr 3 1 3
            r[3] = r[3] + r[1];
            goto next;
        case 34:  // seti 0 9 0
            r[0] = 0;
            goto next;
        case 35:  // seti 0 5 2
            r[2] = 0;
            goto next;
    }

    abort();
}

int main()
{
    printf("Part 1: %llu\n", run(0ull));
    printf("Part 2: %llu\n", run(1ull));
}
