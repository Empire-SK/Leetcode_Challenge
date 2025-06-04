class Solution(object):
    def findDuplicates(self, nums):
        result = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0:
                result.append(abs(num))  # Found a duplicate
            else:
                nums[index] *= -1  # Mark as visited
        return result