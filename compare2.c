#include<cs50.h>
#include<stdio.h>

int main (void)
{
    int x = get_int ("insert first number  \n");
    int y = get_int ("insert second number  \n");
if (y<x)
{
    print (" x is greater than y \n");
}
if (y>x)
{
    print ("y is greater than x \n");
}
else
{
    print ("y is eaqual to x  \n");
}