#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int start=0;
    do
    {
    start = get_int("Enter Start: \n");
    }
    while (start < 9);

    // TODO: Prompt for end size

    int end =0;
    do
    {
    end = get_int("enter End: \n");
    }
    while (end <9);
    // TODO: Calculate number of years until we reach threshold

    int c = (end/4 - start/3 );

    // TODO: Print number of years
    {
        printf("%i \n", c);
    }
}
