class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
        actual_sum = sum(nums)  # Sum of numbers in the array
        return expected_sum - actual_sum  # Missing number