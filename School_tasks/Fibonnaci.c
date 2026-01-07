#include <stdio.h>
 int main() {    
 int n, first = 0, second = 1, next, i;    
 printf("Enter the number of terms: ");  
   scanf("%d", &n);  
   printf("Fibonacci Series: ");      
   printf("\n%d \n%d", first, second);   
      for (i = 2; i < n; i++){ // Calculate and print the remaining terms 
            next = first + second; 
             printf("\n%d", next);            
             first = second;         
             second = next; 
        } 
        printf("\n"); 
    return 0; 
} 
