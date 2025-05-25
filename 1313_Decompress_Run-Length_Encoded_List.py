class Solution(object):
    def decompressRLElist(self, nums):
        result = []
        for i in range(0,len(nums),2):
            freq,val = nums[i],nums[i+1]
            result.extend([val] * freq)
        return result