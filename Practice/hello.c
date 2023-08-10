#include <cs50.h>
#include <stdio.h>

#include <stdio.h>

int main(void)
{
    int n = get_int ("How many array grid do you want to see? \n");
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}