#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int starter;

    while (starter > 9)
    {
    starter = get_int("Enter Start: \n");
    }

    // TODO: Prompt for end size

    int end;
    while (end > 9)
    {

    end = get_int("enter End: \n");

    }

    // TODO: Calculate number of years until we reach threshold

    int a = (start/3);
    int b = (end/4);
    int c = (b - a);

    // TODO: Print number of years
}
