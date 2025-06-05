class Solution(object):
    def majorityElement(self, nums):
        candidate = -1
        votes = 0  # Fixed variable name

        # Finding majority candidate
        for i in range(len(nums)):  
            if votes == 0:
                candidate = nums[i]  # Fixed array name
                votes = 1
            else:
                if nums[i] == candidate:  # Fixed array name
                    votes += 1
                else:
                    votes -= 1
        
        count = 0

        # Checking if majority candidate occurs more than n/2
        # times

        for i in range(len(nums)):  
            if nums[i] == candidate:  # Fixed array name
                count += 1
            
        if count > len(nums) // 2:  # Fixed condition (used len(nums) instead of n)
            return candidate
        else:
            return -1