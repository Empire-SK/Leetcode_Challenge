#include <stdbool.h>
#include <math.h>

// Function to check if a number is prime
bool isPrime(int num) {
    if (num < 2) return false;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}

// Function to check if n has exactly three divisors
bool isThree(int n) {
    int root = sqrt(n);
    return (root * root == n) && isPrime(root);
}

//OPTIMAL SOLUTION