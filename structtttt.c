#include <stdio.h>

struct big {
    char *men;
    int y;
    int x;};
struct smaller{
    char*women;
    struct big a;
};

int main() {
struct smaller part = {"men", "women", 100, 200};

    printf("the number of %s is %d and the number of %s is %d\n", part.a.men, part.a.x, part.women, part.a.y);

    return 0;
}
