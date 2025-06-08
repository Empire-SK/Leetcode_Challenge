from collections import Counter
class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = {}
        n = len(nums)

        for num in nums:
            if num in counter:
                return num
            else:
                counter[num] = 1
        