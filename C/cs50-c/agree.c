#include <cs50.h>
#include <stdio.h>

int main(void)
{
    /*printf("Do you agree? Type 'y' for yes, 'n' for no: ");*/
    /*char c = getchar();*/
    char c = get_char("Do you agree? ");

    if (c == 'y' || c == 'Y')
    {
        printf("Agreed.\n");
    }
    else if (c == 'n' || c == 'N')
    {
        printf("Not agreed.\n");
    }
}