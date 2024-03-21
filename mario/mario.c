#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    int count = 0;

    // Prompt user for Height of Pyramid with a limit of 5 tries to prevent session overstay
    do
    {
        if (count == 4)
        {
            printf("You have one more try \n");
        }
        height = get_int("Enter Pyramid Height  \n");
        count++;
    } while ((height < 1 || height > 8) && count < 5);

    // Print the pyramid
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height - i - 1; j++)
        {
            printf(" ");
        }
        for (int k = 0; k <= i; k++)
        {
            printf("x");
        }
        printf("\n");
    }

    return 0;
}
