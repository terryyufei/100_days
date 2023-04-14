#include <stdio.h>

/**
 * main - prints all the arguments
 *
 * Return: 0
 */

int main(int argc, char **argv)
{
	int i;

	for (i = 0; argv[i] != NULL; i++)
	{
		printf("Argument %d: %s\n", i, argv[i]);
	}
	return (0);
}
