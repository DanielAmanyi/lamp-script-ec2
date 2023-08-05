#include<cs50.h>
#include<stdio.h>

int get_size(void);

int main(void)
{
    int n;

    for (int x = 0; x<6; x++)
    {
        printf ("Hello \n");
    }


    n = grid_size();

    // get grid size

    {
        get_size(void)
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

    return n;
}

