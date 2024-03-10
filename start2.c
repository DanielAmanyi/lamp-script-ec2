#include<stdio.h>
#include<cs50.h>

int main(void)
{
 int a = get_int("Enter your grid size \n");

for (int i = 0; i < a; i++)
{
    for (int j = 0; j<a; j++)
    {
    printf("x");
    }
    printf("\n");
}
}

