#include <stdio.h>
#include <stdlib.h>

int main() {
    int *ptr;

    // Allocate memory for an integer
    ptr = (int*)malloc(sizeof(int));

    // Assign a value to the allocated memory
    *ptr = 10;

    // Use the value
    printf("Value: %d\n", *ptr);

    // Deallocate the memory
    free(ptr);

    return 0;
}