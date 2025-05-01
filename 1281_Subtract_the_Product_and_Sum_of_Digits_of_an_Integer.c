int subtractProductAndSum(int n) {
    int product = 1; // Initialize product to 1 (not 0, as multiplying by 0 gives 0)
    int sum = 0;     // Initialize sum to 0
    
    // Process each digit
    while (n > 0) {
        int digit = n % 10;  // Extract the last digit
        product *= digit;    // Update product
        sum += digit;        // Update sum
        n /= 10;             // Remove the last digit from n
    }
    
    return product - sum;
}