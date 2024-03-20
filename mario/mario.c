#include<cs50.h>
#include<stdio.h>

// Declare variables
int main(void){
int height;
int count = 0;


// Prompt user for Height of Pyramid with a limit of 5 tries to prevent session overstay
do{
    if (count == 4){
     printf("You have one more try \n");
    }
height = get_int("Enter Pyramid Height  \n");


count++;
}
while ((height <1 || height >8) && count <5);
















    return 0;
}
