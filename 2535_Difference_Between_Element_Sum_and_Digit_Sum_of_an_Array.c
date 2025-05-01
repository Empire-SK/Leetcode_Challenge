int differenceOfSum(int *nums, int numsSize)
{
    int element = 0;
    int sum = 0;

    for (int i = 0; i < numsSize; i++)
    {
        sum += nums[i];
        while (nums[i] > 0)
        {
            int digit = nums[i] % 10;
            element += digit;
            nums[i] /= 10;
        }
    }
    return abs(element - sum);
}