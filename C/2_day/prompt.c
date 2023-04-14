#include <stdio.h>
#include <stdlib.h>

/**
 * main - prints $, waits for user to enter command
 *
 * Return : 0
 */

int main(void)
{
	char *command = NULL;
	size_t len = 0;
	ssize_t read;

	while (1)
	{
		printf("$");
		read = getline(&command, &len, stdin);

		if (read != -1)
		{
			printf("%s", command);
		}
		else
		{
			printf("Error reading input.\n");

			break;
		}
	}
	free(command);
	return (0);
}
