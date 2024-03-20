#include<stdio.h>
#include<cs50.h>


int main(void){
// char name[25];


string name = get_string("Whats your name? \n");


// printf("Hello, What's your name ? \n");
// scanf("%s25", name);


printf("Hello, %s \n", name);


    return 0;
}
