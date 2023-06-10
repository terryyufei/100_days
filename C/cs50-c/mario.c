#include <stdio.h>
#include <cs50.h>

/*print a 4 by 4 grid*/

int main(void)
{
    int i, j;
    /*const int n = 4;*/
    int n = get_int("Size: ");

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}