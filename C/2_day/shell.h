#ifndef SHELL_H
#define SHELL_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

char **splitstring(char *str, const char *delim, int *count);
char **split_string(const char *str, int *count);
#endif
