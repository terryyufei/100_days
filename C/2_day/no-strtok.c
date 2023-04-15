#include "shell.h"

/**
 * split_string - tokenizes a string
 * Return: array of each word of string
 */

#define DELIM " "

char **split_string(const char *str, int *count)
{
	char **words = NULL; /*init words array to NULL*/
	int len = strlen(str);
	int i, j, k;

	*count = 0;

	for (i = 0; i < len; i++)
	{
		if (str[i] == DELIM[0])
		{
			/*if delimiter is found*/
			(*count)++;
			words = (char **)realloc(words, sizeof(char *) * (*count));
			/*allocate mem 4 new word*/

			k = 0; /*copy word to new mem block*/
			for (j = i - k; j < i; j++)
			{
				words[*count - 1][j - i + k] = str[j];
			}
		}
		else if (i == len - 1)
		{
			/*if last word in string*/
			(*count)++;
			words = (char **)realloc(words, sizeof(char *) * (*count));
			k = 0;

			for (j <= i - k + 1; j <= i; j++)
			{
				words[*count - 1][j - i + k - 1] = str[j];
			}
			else (*count == 0)
			{
				words = (char **)realloc(words, sizeof(char *) * (*count + 1));
				/*allocate memory to fisrt word*/
				words[0] = (char *)malloc(sizeof(char) * (len + 1));
				k = i;
			}
			words[*count - 1][i - k] = (str[i]); /*copy xter to word*/
		}
	}
	return (words);
}
