#include <stdio.h>
#include <math.h>

float findtheaverage(float a, float b, float c, float d) {
    float z = fmaf(a + b + c, 1.0, d) / 4;
    return z;
}

int main() {
    float a, b, c, d, average;

    printf("Enter score for a: ");
    scanf("%f", &a);

    printf("Enter score for b: ");
    scanf("%f", &b);

    printf("Enter score for c: ");
    scanf("%f", &c);

    printf("Enter score for d: ");
    scanf("%f", &d);

    average = findtheaverage(a, b, c, d);

    printf("The average is: %.2f", average);

    return 0;
}
