class Solution(object):
    def sortedSquares(self, nums):
        x=[]
        for i in range(len(nums)):
            x.append(nums[i]**2)
        return sorted(x)