#include <cs50.h>
#include <stdio.h>

int main(void)

{
    string input_last_name = get_string ("what is your Last name?  ");
    string input_first_name = get_string ("what is your First name?  ");
    printf ("Hello, and welcome %s %s\n", input_last_name, input_first_name);

}