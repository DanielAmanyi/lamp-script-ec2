#include<cs50.h>
#include<stdio.h>

int main (void)

{
    const int n = get_int ("enter grid size \n");
    for (int g = 0; g < n; g++)
    {
        for (int f = 0; f < n; f++)
        {
            printf ("*");
        }

        printf (" \n");
    }
}