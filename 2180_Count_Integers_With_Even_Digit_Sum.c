int countEven(int num) {
    int count = 0;

    for (int i = 1; i <= num; i++) {
        int sum = 0, temp = i;

        // Calculate the sum of digits
        while (temp > 0) {
            sum += temp % 10;
            temp /= 10;
        }

        // Check if digit sum is even
        if (sum % 2 == 0) {
            count++;
        }
    }
    
    return count;
}