#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int start;
    do
    {
    start = get_int("Enter Start: \n");
    }
    while (start < 9);

    // TODO: Prompt for end size

    int end;
    do
    {
    end = get_int("enter End: \n");
    }
    while (end <start);
    // TODO: Calculate number of years until we reach threshold

    int c = 0;
        start = start + (start/4 - start/3 );
        c++;

    // TODO: Print number of years
    {
        printf("Years: %i \n", c);
    }
}
