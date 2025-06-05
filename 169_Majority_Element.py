class Solution(object):
    def majorityElement(self, nums):
        majority=nums[0]
        count=0

        for x in nums:
            if count== 0:
                majority=x

            if x==majority:
                count +=1
            else:
                count -=1

        count=0
        for x in nums:
            if x == majority:
                count +=1

        if count>len(nums)//2:
            return majority