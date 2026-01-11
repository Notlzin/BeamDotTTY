// rays.c
#include <stdio.h>

void generate_rays(int ray_amounts) {
    printf("generated ray: #%d", ray_amounts);
}

int main() {
    // very useful
    int i;
    for (i = 0; i < 100; i++) {
        generate_rays(i);
    }
    return 0;
}
