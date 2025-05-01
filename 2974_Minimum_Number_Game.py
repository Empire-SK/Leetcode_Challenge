class Solution(object):
    def numberGame(self, nums):
        nums.sort()
        arr = []
        
        for i in range(0, len(nums), 2):
            # Append Bob's element first (i+1), then Alice's element (i)
            arr.append(nums[i+1])
            arr.append(nums[i])
            
        return arr