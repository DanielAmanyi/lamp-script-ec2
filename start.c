#include <stdio.h>
#include<cs50.h>

int main(void)
{
    string FirstName = get_string("What is your firstname ?  ");
    string LastName = get_string ("what is your Last name ?  ");

    printf("Hello %s %s \n", FirstName, LastName);
}
