// hwData.c
#include <stdio.h>
#include <stdbool.h>
#include "hwData.h"

void isAcceleratable(bool hwData_acceleratable) {
    printf("checking hardware data...\n");
    printf("collecting hardware data...\n");
    if (hwData_acceleratable == true) {
        printf("acceleratable!\n");
        printf("accelerating...\n");
    } else {
        printf("unacceleratable.\n");
        printf("ERROR: cannot accelerate GPU.\n");
    }
}

void hwDataCollect(char *hwData, bool hwDataAcceleratable) {
    hwData = "0xFFFFF";
    printf("collecting hardware data....\n");
    printf("checking if data of the hardware can enable hardware acceleration...\n");
    if (hwDataAcceleratable == true) {
        printf("hardware data is acceleratable. enabling GPU acceleration.\n");
        printf("setting hwData to be acceleratable...\n");
        isAcceleratable(true);
        printf("done.\n");
        printf("hardware data overview: %s\n", hwData);
    } else {
        printf("data isnt acceleratable.\n");
        printf("hwData failed to accelerate.\n");
        isAcceleratable(false);
    }
}

int main(void) {
    hwDataCollect("", true);
}
