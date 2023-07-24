#include <stdio.h>
#include <cs50.h>
/*
int main(void)
{
    int scores[3];
    scores[0] = 72;
    scores[1] = 73;
    scores[2] = 33;
    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / 3.0);
}*/

/*
int main(void)
{
    int scores[3];
    int i;

    for (i = 0; i < 3; i++)
    {
        scores[i] = get_int("Scores: ");
    }

    printf("Average: %f\n", (scores[0] + scores[1] + scores[2]) / (float) 3);
}
*/

float average( int array[]);
const int N = 3;

int main(void)
{
    int scores[N];
    int i;

    for (i = 0; i < 3; i++)
    {
        scores[i] = get_int("Scores: ");
    }

    printf("Average: %f\n", average(scores));
}

float average(int array[])
{
    int sum = 0;
    int i;

    for (i = 0; i < N; i++)
    {
        sum += array[i];
    }
    return sum / (float) N;
}