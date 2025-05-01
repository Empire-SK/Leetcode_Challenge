class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}  # Store value: index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:  # Check if complement was seen before
                return [hash_map[complement], i]  # Return stored index and current index
            hash_map[num] = i  # Store current number and its index