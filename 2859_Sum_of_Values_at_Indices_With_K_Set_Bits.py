class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        result = 0
        for i in range(len(nums)): 
            if bin(i).count('1') == k: 
                result += nums[i]  
        return result