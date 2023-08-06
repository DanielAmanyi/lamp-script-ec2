#include <stdio.h>
#include <cs50.h>


int main(void)
{
int x = get_int ("input first value ");
int y = get_int ("input second value ");
if (x<y)
{
printf ( "x is less than y . \n");
}
else if (x>y)
{
    printf ( "y is greater than x \n");
}
else
{
    printf("x is eaqual to y");
}
}