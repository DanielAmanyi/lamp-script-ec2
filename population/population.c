#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start_size;

    do
    {
        start_size = get_int (" Enter Starting Population \n");
    }
    while (start_size < 9);



    // TODO: Prompt for end size
     int end_size;

    do
    {
        end_size = get_int (" Enter ending Population \n")
    }
    while (end_size < 9);

    return 0;
    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}
