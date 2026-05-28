class Solution(object):
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        current = 0
        for i in range(n):
            current += i * nums[i]
        maximum = current
        for k in range(1, n):
            current = (
                current
                + total_sum
                - n * nums[n - k]
            )
            maximum = max(maximum, current)
        return maximum
        