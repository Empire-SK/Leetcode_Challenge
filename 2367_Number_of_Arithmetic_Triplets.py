class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        seen = set(nums)
        count = 0
        for num in nums:
            if num + diff in seen and num + 2 * diff in seen:
                count += 1
        return count