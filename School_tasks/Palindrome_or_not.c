#include <stdio.h> 
#include <string.h>  
void main() { 
  char str[100];   
   int i, len, flag;   
 flag = 0; 
 printf("\n Please Enter any String :  ");
 fgets(str, sizeof(str), stdin);    	
 len = strlen(str);
 for(i = 0; i < len; i++) {
 	 	if(str[i] != str[len - i - 1]) { 
 	 	 	flag = 1; 
 	 	 	break; 	 
 	 	 }  
 	 } 
 	 if(flag == 0) { 
 	  printf("\n %s is a Palindrome String", str); 
 	 } 
 	 else 
 	 {    
      printf("\n %s is Not a Palindrome String", str); 
 	} 	
	
} 
