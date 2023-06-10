#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("what is x?: ");
    int x = scanf("%d", &x);
    printf("what is y? : ");
    int y = scanf("%d", &y);

    if (x < y)
    {
        printf("x is less than y\n");
    }
    else if (x > y)
    {
        printf(" x is greater than y\n");
    }
    else
    {
        printf("x is equal to y\n");
    }

}