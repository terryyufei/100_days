#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s, t;

    s = get_string("s: ");
    t = get_string("t: ");

    if (strcmp(s, t) == 0)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }

}
