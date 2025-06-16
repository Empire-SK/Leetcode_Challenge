class Solution:
    def findMaxK(self, nums):
        num_set = set(nums)
        candidates = [num for num in num_set if num > 0 and -num in num_set]
        return max(candidates) if candidates else -1