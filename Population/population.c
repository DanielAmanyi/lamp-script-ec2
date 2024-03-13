#include<stdio.h>
#include<cs50.h>

int main(void) {

    // TODO: Prompt for start size

int start = get_int("Enter Start Size \n");

    // TODO: Prompt for end size

int end = get_int("Stop Size \n");

    // TODO: Calculate number of years until we reach threshold
    doubl years;

    years = start * (1/3) + end *(1/4);

    // TODO: Print number of years
    printf(" Lamas left would be %i \n", years);







    return 0;
}
