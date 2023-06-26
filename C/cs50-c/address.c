#include <stdio.h>

int main(void)
{
    int n = 50;
    printf("%p\n", &n);/*prints address of n*/

    int *p = &n;
    printf("%p\n", p); /* prints value of p, which the address of n*/
    
    printf("%i\n", *p); /*prints the value that p is pointing at*/
}


