#include <stdio.h>

int main(void)
{
    char *s = "HI!";
    printf("%s\n", s); /*print value*/
    printf("%p\n", s); /*print address*/

    // pointer arithmetics
    printf("%c\n", *s); // or s[0]
    printf("%c\n", *(s+1)); // or s[1]
    printf("%c\n", *(s+2)); // or s[2]
    printf("%c\n", *(s+3)); // or s[3]

    printf("%s\n", s);
    printf("%s\n", s+1);
    printf("%s\n", s+2);
}
