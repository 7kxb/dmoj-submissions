#include <stdio.h>
#include <time.h>
#include <stdlib.h>
int main() {
    srand(time(NULL));
    printf("%d\n", 1);
    printf("%d\n", 16);
    printf("%d\n", 2);
    for (int i = 0; i < 16; i++) rand();
    printf("%d\n", rand());
}