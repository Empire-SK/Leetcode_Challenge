class Solution(object):
    def sortedSquares(self, nums):
        return sorted([num * num for num in nums])