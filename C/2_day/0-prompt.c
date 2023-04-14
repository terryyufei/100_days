#include <stdio.h>
#include <stdlib.h>
/**
 * main - prints $, wait for the user to enter command
 *
 * Return: 0
 */

int main(void)
{
	char *line = NULL;
	size_t len = 0;

	printf("Enter a line of text:\n");

	ssize_t read = getline(&line, &len, stdin);

	if (read != -1)
	{
		printf("You entered:%s\n", line);
	}
	else
	{
		printf("Erroe reading input.\n");
	}
	free(line);
	return (0);
}
