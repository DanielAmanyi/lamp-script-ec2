#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start_size;

    do
    {
        start_size = get_int("Enter Starting Population: ");
    }
    while (start_size < 9);

    // TODO: Prompt for end size
    int end_size;

    do
    {
        end_size = get_int("Enter ending Population: ");
    }
    while (end_size < 9);

    // Rest of your code...

    return 0;
}
