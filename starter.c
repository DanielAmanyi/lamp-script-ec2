#include<stdio.h>
#include<cs50.h>


int main(void)

{
string firstname = get_string("what's your first name? \n");
string lastname = get_string("your Surname?  \n");
printf("Hello %s, %s" firstname, lastname);
}
