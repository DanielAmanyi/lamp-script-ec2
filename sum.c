#include<cs50.h>
#include<stdio.h>


int sumx ()

{

    int x = 0;
    while (x >=3)
    {
        printf ("Enter your name \n");
    }

    int a = get_int ("Enter First Number: \n");
   int  b = get_int ("Enter Second Number: \n");

   int sumx = (a + b);
   {
    printf("The Sum is: %i \n", sumx);
   }
return sumx;

}
























int main (void)
{
    int y = (2 * sumx());

    printf("%i", y);
}
















