#include <stdio.h>
int main() { 
char ch ; 
printf("Enter a character: "); 
scanf("%c",&ch); 
if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ) { 
  printf("The character %c is a vowel.\n", ch); 
    } 
    else{ 
        printf("The character %c is a consonant.\n", ch); 
    } 
    return 0; 
} 
