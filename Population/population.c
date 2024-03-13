#include<stdio.h>
#include<cs50.h>

int main(void) {

    // TODO: Prompt for start size

int start = get_int("Enter Start Size \n");

    // TODO: Prompt for end size

int end = get_int("Stop Size \n");

    // TODO: Calculate number of years until we reach threshold
    double years;

    years = start/3 + end/4;

    // TODO: Print number of years
    printf(" Lamas left would be %lf \n", years);







    return 0;
}
