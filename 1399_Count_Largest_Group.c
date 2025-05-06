int countLargestGroup(int n) {
    // Since n <= 10^4, maximum digit sum would be 9+9+9+9 = 36
    #define MAX_DIGIT_SUM 40
    
    // Array to store counts of each digit sum
    int counts[MAX_DIGIT_SUM] = {0};
    
    // Calculate digit sum for each number from 1 to n
    for (int i = 1; i <= n; i++) {
        int num = i;
        int sum = 0;
        
        // Calculate digit sum
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        
        counts[sum]++;
    }
    
    // Find the maximum count
    int maxCount = 0;
    for (int i = 1; i < MAX_DIGIT_SUM; i++) {
        if (counts[i] > maxCount) {
            maxCount = counts[i];
        }
    }
    
    // Count how many groups have the maximum size
    int result = 0;
    for (int i = 1; i < MAX_DIGIT_SUM; i++) {
        if (counts[i] == maxCount) {
            result++;
        }
    }
    
    return result;
}