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
        printf("Enter Starting Population: ");
        scanf("%d", &start_size);
        flush_input_buffer(); // Flush the input buffer
    }
    while (start_size < 9);

    // TODO: Prompt for end size
    int end_size;

    do
    {
        printf("Enter ending Population: ");
        scanf("%d", &end_size);
        flush_input_buffer(); // Flush the input buffer
    }
    while (end_size < 9);

    // Rest of your code...

    return 0;
}
