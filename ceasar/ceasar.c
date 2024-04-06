#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

void cipher_text(string plaintext, int key);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]);

    printf("Success\n%d\n", key);

    string plaintext = get_string("Plaintext: ");

    printf("Ciphertext: ");

    cipher_text(plaintext, key);

    printf("\n");

    return 0;
}

void cipher_text(string plaintext, int key)
{
    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (islower(plaintext[i]))
        {
            printf("%c", 'a' + (plaintext[i] - 'a' + key) % 26);
        }
        else if (isupper(plaintext[i]))
        {
            printf("%c", 'A' + (plaintext[i] - 'A' + key) % 26);
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
}
