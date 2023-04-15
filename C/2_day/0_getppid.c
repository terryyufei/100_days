#include <stdio.h>
#include <unistd.h>

/**
 * main - PPID
 *
 * Return: always 0
 */

int main(void)
{
	pid_t my_pid, ppid;

	my_pid = getpid();
	printf("PID: %u\n", my_pid);

	ppid = getppid();
	printf("PPID: %u\n", ppid);
	return (0);
}
