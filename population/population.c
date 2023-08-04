#include <cs50.h>
#include <stdio.h>

void flush_input_buffer()
{
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main(void)
{
    // TODO: Prompt for start size
    int start_size;

    do
    {
        start_size = get_int("Enter Starting Population: ");
        flush_input_buffer(); // Flush the input buffer
    }
    while (start_size < 9);

    // TODO: Prompt for end size
    int end_size;

    do
    {
        end_size = get_int("Enter ending Population: ");
        flush_input_buffer(); // Flush the input buffer
    }
    while (end_size < 9);

    // Rest of your code...

    return 0;
}
