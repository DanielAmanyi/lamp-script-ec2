#include<cs50.h>
#include<stdio.h>


int main (void)
{
// int scores = get_int("enter score \n");

int scores[3];
// scores[0] = get_int("Score1: \n");
// scores[1] = get_int("Score2: \n");
// scores[2] = get_int("Score3: \n");
int n=3;
for (int i=0; i<n; i++)
{
   scores[n] = get_int("enter score \n");
}

{
    printf("Average Equals:  %d \n", (scores[1] + scores[0] + scores[2] )/n);
}



    return 0;
}
