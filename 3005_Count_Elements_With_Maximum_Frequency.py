class Solution(object):
    def maxFrequencyElements(self, nums):
        FreeQ={}
        Count_Val=0
        for i in nums:
            if i in FreeQ:
                FreeQ[i]+=1
                
            else:
                FreeQ[i]=1
        
        #i will be finding the highest freequncy 
        max_freequency=max(FreeQ.values())

        total=0
        for val in FreeQ.values():
            if val == max_freequency:
                total+=val
        return total