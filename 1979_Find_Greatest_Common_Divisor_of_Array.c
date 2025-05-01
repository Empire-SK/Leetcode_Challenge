int findGCD(int* nums, int numsSize) {
    int i, s, b;
    s = b = nums[0];  // Initialize both to the first element

    // Find smallest and largest numbers in one pass
    for (i = 1; i < numsSize; i++) {
        if (nums[i] < s) s = nums[i];
        if (nums[i] > b) b = nums[i];
    }

    // Find GCD using a decreasing loop approach
    for (i = s; i >= 1; i--) {
        if (s % i == 0 && b % i == 0)
            return i;
    }

    return 1; // Default case
}