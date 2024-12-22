#include <stdio.h>

// Initializing A Function
void hello(char user[]);
int sum(int x, int y);
float division(int x, int y);

int main(){
    // Call A Function
    hello("SALAH\n");
    printf("%d", sum(1, 1));
    printf("%f", division(1, 1));

    return 0;
}

// A Function
void hello(char user[]){
    printf("Hello, %s", user);
}
int sum(int x, int y){
    return x + y;
}
float division(int x, int y){
    return x / y;
}
