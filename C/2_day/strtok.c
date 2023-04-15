#include "shell.h"

/**
 * splitstring - splits string and return an array of each word of
 * the string
 * @str: pointer to the string being split
 * @delim: delimiter to split the string by
 * @count: pointer to an int holding the number of words in the resluting array of strings
 *
 * Return: array of each word
 */

char **splitstring(char *str, const char *delim, int *count)
{
	char **words = NULL;

	char *token = strtok(str, delim);
	*count = 0;

	while (token != NULL)
	{
		(*count)++;
		words = (char**)realloc(words, sizeof(char*) * (*count));
		words[*count -1] = token;
		token = strtok(NULL, delim);
	}
	return (words);
}

/**
 * main - contains the string
 * Return: 0
 */

int main(void)
{
	char str[] = "Hello world! This is a string.";
	const char delim[] = " ";
	int count = 0;

	char ** words = splitstring(str, delim, &count);

	for (int i = 0; i < count; i++)
	{
		printf("%s\n", words[i]);
	}
	free(words);
	return (0);
}
