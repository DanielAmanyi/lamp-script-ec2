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

    start_years = start/3;
    end_years = end/4;
    Total_lamas = end_years - start_years;

    // TODO: Print number of years
    printf(" Lamas left would be %lf \n", Total_lamas);







    return 0;
}
