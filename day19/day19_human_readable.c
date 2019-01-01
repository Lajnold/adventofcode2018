#include <stdio.h>

int f(int big)
{
    int target = 0;
    target += 2;
    target *= target;
    target *= 19;
    target *= 11;
    target += ((6 * 22) + 6);
    if (big) {
        int additional = 27;
        additional *= 28;
        additional += 29;
        additional *= 30;
        additional *= 14;
        additional *= 32;
        target += additional;
    }

    int div1 = 1;
    int div2 = 1;
    int div_sum = 0;

    while (div1 <= target) {
        div2 = 1;
        
        while (div2 <= target) {
            // Cast to avoid multiplication overflow.
            if ((unsigned long long) div1 * (unsigned long long) div2 == (unsigned long long) target) {
                div_sum += div1;
            }
            div2++;
        }

        div1++;
    }

    return div_sum;
}

int main()
{
    printf("Part 1: %d\n", f(0));
    printf("Part 2: %d\n", f(1));
}
