#include <stdio.h>

int main() {
    int primes[50], count = 0, sum = 0;
    int *ptr = primes;

    for (int i = 50; i <= 100; i++) {
        int is_prime = 1;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                is_prime = 0;
                break;
            }
        }

        if (is_prime) {
            *ptr = i;
            ptr++;
            count++;
            sum += i;
        }
    }

    printf("Prime numbers between 50 and 100:\n");
    for (int i = 0; i < count; i++) {
        printf("%d ", primes[i]);
    }
    printf("\n\nCount of prime numbers: %d\n", count);
    printf("Sum of prime numbers: %d\n", sum);

    return 0;
}

