#include<stdio.h>
#include<cs50.h>

int main (void)
{
    int x = get_int ("insert first number  \n");
    int y = get_int ("insert second number  \n");
if (y<x)
{
    printf ( " x is greater than y \n");
}
if (y>x)
{
    printf ( "y is greater than x \n");
}
else
{
    printf ( "y is eaqual to x  \n");
}
}