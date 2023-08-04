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

}