#include "shell.h"

/**
 * main - entry point
 *
 * Return : 0
 */

#define MAX_PATH_LEN 1024

int main(int argc, char *argv[])
{
	char *path_env = getenv("PATH");
	char *path = strtok(path_env, ":");

	while (path != NULL)
	{
		char full_path[MAX_PATH_LEN];
		snprintf(full_path, MAX_PATH_LEN,"%s/%s", path, argv[1]);

		if (access(full_path, F_OK) == 0)
		{
			printf("%s\n", full_path);
			return (0);
		}
		path = strtok(NULL, ":");
	}
	printf("%s not found in PATHA\n", argv[1]);
	return (1);
}
