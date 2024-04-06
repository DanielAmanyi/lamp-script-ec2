#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

// Function prototype
void cipher_text(string plaintext, int key);

int main(int argc, string argv[])
{
    // Check if the program is executed with the correct number of arguments
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Check if the argument (key) is a valid positive integer
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    // Convert the argument (key) to an integer
    int key = atoi(argv[1]);

    // Print the key for verification
    printf("Success\n%d\n", key);

    // Get the plaintext from the user
    string plaintext = get_string("Plaintext: ");

    // Print the header for the ciphertext
    printf("Ciphertext: ");

    // Encrypt the plaintext and print the ciphertext
    cipher_text(plaintext, key);

    printf("\n");

    return 0;
}

// Function to encrypt the plaintext using the Caesar cipher with the given key
void cipher_text(string plaintext, int key)
{
    // Iterate through each character in the plaintext
    for (int i = 0; i < strlen(plaintext); i++)
    {
        // Check if the character is a lowercase letter
        if (islower(plaintext[i]))
        {
            // Encrypt the lowercase letter and print the ciphertext
            printf("%c", 'a' + (plaintext[i] - 'a' + key) % 26);
        }
        // Check if the character is an uppercase letter
        else if (isupper(plaintext[i]))
        {
            // Encrypt the uppercase letter and print the ciphertext
            printf("%c", 'A' + (plaintext[i] - 'A' + key) % 26);
        }
        // If the character is not a letter, print it as is
        else
        {
            printf("%c", plaintext[i]);
        }
    }
}
