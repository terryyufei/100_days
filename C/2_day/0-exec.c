#include "shell.h"

/**
 * main - a function that executes a program
 *
 * Return: 0
 */

int main(void)
{
	char *args[] = {"ls", "-l", NULL};
	char *envp[] = {NULL};

	printf("Before execve\n");

	if (execve("/bin/ls", args, envp) == - 1)
	{
		perror("execve");

		exit(EXIT_FAILURE);
	}
	printf("This line will not be executed\n");

	return (0);
}
