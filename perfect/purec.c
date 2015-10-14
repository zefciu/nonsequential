#include <stdio.h>

int is_perfect(unsigned long n) {
    unsigned long i, sum=0;
    for (i=1; i < n; i++) {
        if (n % i == 0) {
            sum += i;
        }
    }
    return sum == n;
}

int main(int argc, char** argv) {
    unsigned long i;
    for (i = 0; i < 100000; i++) {
        if (is_perfect(i)) {
            printf("%lu\n", i);
        }
    }
}
