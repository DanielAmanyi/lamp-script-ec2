#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

#include <string.h>


void encrypt(string plaintext, int key);

int main(int argc, string argv[])
{
    // Check for correct number of command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check if all characters in the argument are digits
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Convert the key from string to an integer
    int key = atoi(argv[1]);

    // Get plaintext input from user
    string plaintext = get_string("plaintext: ");

    // Encrypt the plaintext and output the ciphertext
    printf("ciphertext: ");
    encrypt(plaintext, key);
    printf("\n");

    return 0;
}

void encrypt(string plaintext, int key)
{
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        char encrypted_char = plaintext[i];

        if (isalpha(plaintext[i]))
        {
            char base = isupper(plaintext[i]) ? 'A' : 'a';
            encrypted_char = ((plaintext[i] - base + key) % 26) + base;
        }

        printf("%c", encrypted_char);
    }
}
