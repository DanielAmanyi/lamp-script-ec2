#include<stdio.h>
#include<cs50.h>

int main(void)
{
int first_number = get_int ("Please enter your first number \n");
int second_number = get_int ("Please enter your second number \n");

if (first_number<second_number)
{
printf("Second Number is Larger \n");
}
if (first_number>second_number)
{
printf ("First number is Larger \n");
}
else
{printf("both numbers are equal \n");
}
}