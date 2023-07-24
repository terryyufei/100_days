#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <ctype.h>

/**
 * main - entry point
 * get input from user and change it to uppercase
*/
/*
int main(void)
{
    int i;
    string s = get_string("Before: ");
    printf("After:  ");

    for (i = 0; i < strlen(s); i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", s[i] - 32);
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
} */

int main(void)
{
    int i;
    string s = get_string("Before: ");
    printf("After:  ");

    for (i = 0; i < strlen(s); i++)
    {
        if (islower(s[i]))
        {
            printf("%c", toupper(s[i]));
        }

    }
    printf("\n");
}

/*ctype.h has islower() and toupper()*/