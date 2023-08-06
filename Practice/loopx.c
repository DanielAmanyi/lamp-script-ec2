#include<cs50.h>
#include<stdio.h>

int main(void)
{
       int n;
    for (int x = 1; x<20; x= x+ 2)
    {
        printf (" %i\n", x);
    }

    do
    {

    n = get_int ("How many Tualey do you want to see ? \n");

    }
    while (n <= 2);

    for (int y = 0; y < n; y++)
    {
        printf("Tualey \n");
    }
}

