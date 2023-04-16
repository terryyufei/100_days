#include "shell.h"

/**
 * main - entry point
 *
 * Return:
 */

int main(void)
{
	int i;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();

		if (pid == -1)
		{
			perror("fork error");

			exit(EXIT_FAILURE);
		}
		else if (pid == 0)
		{
			execl("/bin/ls", "ls", "-l", "/tmp", (char *) NULL);
			exit(EXIT_FAILURE);
		}
		else
		{
			wait(NULL);
		}
	}
	return (0);
}

