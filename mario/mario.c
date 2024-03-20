#include<cs50.h>
#include<stdio.h>

int main(void){
int height;
int count = 0;


do{
    if (count == 4){
     printf("You have one more try \n");
    }
height = get_int("Enter Pyramid Height  \n");




}
while (height <1 || height >8 ||count <5);
















    return 0;
}
