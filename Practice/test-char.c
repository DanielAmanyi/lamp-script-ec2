#include<stdio.h>
#include<cs50.h>

int main(void)
{
    char c = get_char ("enter character \n");
    if (c == 'y' || c =='Y')
    {
        printf ("Agreed \n");
    }
        else if (c == 'n' || c=='N')

        {
            printf ("Disagreed \n");
        }

        else
        {
            printf ("INVALID ENTRY \n");
        }
    
}