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

    int a = (start/3);
    int b = (end/4);
    int c = (b - a);

    // TODO: Print number of years
}
