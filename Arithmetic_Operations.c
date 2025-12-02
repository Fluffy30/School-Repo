#include <stdio.h>
void main() {
    int a, b, sum, multi, divide, num;
    printf("Enter a and b values: ");
    scanf("%d %d", &a, &b);
    printf("Enter your choice:\n1.Addition\n2.Multiplication\n3.Division\n");
    scanf("%d", &num);
    switch(num) {
        case 1:
            sum = a + b;
            printf("Sum: %d\n", sum);
            break;
        case 2:
            multi = a * b;
            printf("Multiplication: %d\n", multi);
            break;
        case 3:
            if(b != 0) {
                divide = a / b;
                printf("Division: %d\n", divide);
            } else {
                printf("Error: Division by zero is not allowed.\n");
            }
            break;
        default:
            printf("Invalid choice.\n");
    }
        }