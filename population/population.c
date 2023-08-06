#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int start=0;

    while (start > 9)
    {
    start = get_int("Enter Start: \n");
    }
    return start;
    // TODO: Prompt for end size

    int end =0;
    while (end > 9)
    {
    end = get_int("enter End: \n");
    }
    return end;
    // TODO: Calculate number of years until we reach threshold

    int a = (start/3);
    int b = (end/4);
    int c = (b - a);

    // TODO: Print number of years
}
