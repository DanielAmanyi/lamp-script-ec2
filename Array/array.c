#include<cs50.h>
#include<stdio.h>


int main (void)
{

// int scores = get_int("enter score \n");

int scores[3];
for (int i=0; i<3; i++);
{
    scores = get_int("enter score \n");
}

{
    printf("%d \n", (scores[1] + scores[0] + scores[2] )/3);
}



    return 0;
}
