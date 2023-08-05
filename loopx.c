#include<cs50.h>
#include<stdio.h>

int main(void)
{
   for (int x = 0; x<6; x++)
    {
        printf ("Hello \n");
    }

    int n = get_int ("How many Tualey do you want to see ? \n");

    for (int y = 0; y < n; y++)
    {
        printf("Tualey \n");
    }
}

