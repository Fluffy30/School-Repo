#include <stdio.h>
int main(){
    int n, i;
    int fact = 1;
    printf("Enter an interger: ");
    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        fact = fact * i;
    }
    printf("Factorial of %d is %d\n", n, fact);
    return 0;
    
}