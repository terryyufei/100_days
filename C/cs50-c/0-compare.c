#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int i, j;

    i = get_int("i: ");
    j = get_int("j: ");

    if (i == j)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }

}
