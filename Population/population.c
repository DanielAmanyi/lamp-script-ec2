#include<stdio.h>
#include<cs50.h>

int main(void) {

    // TODO: Prompt for start size

int start = get_int("Enter Start Size \n");

    // TODO: Prompt for end size

int end = get_int("Stop Size \n");

    // TODO: Calculate number of years until we reach threshold
    double start_years, end_years;
    int Total_lamas;
    int years;

    start_years = start/3;
    end_years = start/4;
    Total_lamas = end_years - start_years;
    years = start+Total_lamas;

    // TODO: Print number of years
    printf(" Lamas left would be %i \n", years);







    return 0;
}
