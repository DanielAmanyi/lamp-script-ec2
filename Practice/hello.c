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
    int x;
    int y = get_int ("How many Stars do you want to see? \n");
   for (x=0; x<=y; x++)
   {
    printf("*");
   }
   return 0;
}