#include <stdio.h>
#include<cs50.h>

int main(void)
{
    string FirstName = get_string("What is your firstname ?  ");
    string LastName = get_string ("what is your Last name ?  ");
    string MiddleName = get_string ("what's your middle name ?");

    printf("Hello %s %s %s \n", LastName, FirstName, MiddleName);
}
