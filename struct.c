#include <stdio.h>
struct big {
    char *men;
    char *women;
    int x;
    int y;
};

int main() {
struct big part = {"men", "women", 100, 201};
printf("the number of %s is %d and the number of %s is %d\n", part.men, part.x, part.women, part.y);
return 0;
}
