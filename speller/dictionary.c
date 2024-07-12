// dictionary.c

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include "dictionary.h"

// Define the size of the hash table
#define HASHTABLE_SIZE 65536

// Define the maximum length for a word
#define LENGTH 45

// Node structure for linked list
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Hash table
node *hashtable[HASHTABLE_SIZE];

// Hash function (djb2)
unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int c;

    while ((c = *word++))
    {
        hash = ((hash << 5) + hash) + tolower(c); // hash * 33 + c
    }

    return hash % HASHTABLE_SIZE;
}

// Number of words in dictionary
unsigned int word_count = 0;

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary file
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    // Buffer for a word
    char word[LENGTH + 1];

    // Read words from the dictionary file
    while (fscanf(file, "%45s", word) != EOF)
    {
        // Create a new node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            return false;
        }
        strcpy(new_node->word, word);
        new_node->next = NULL;

        // Hash the word to obtain a hash value
        unsigned int index = hash(word);

        // Insert the node into the hash table
        if (hashtable[index] == NULL)
        {
            hashtable[index] = new_node;
        }
        else
        {
            new_node->next = hashtable[index];
            hashtable[index] = new_node;
        }

        // Increment word count
        word_count++;
    }

    // Close the dictionary file
    fclose(file);

    return true;
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to obtain a hash value
    unsigned int index = hash(word);

    // Access linked list at that index
    node *cursor = hashtable[index];

    // Traverse linked list and compare words (case-insensitively)
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < HASHTABLE_SIZE; i++)
    {
        node *cursor = hashtable[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
    }

    return true;
}
