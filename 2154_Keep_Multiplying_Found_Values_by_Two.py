class Solution(object):
    def findFinalValue(self, nums, original):
        while original in nums:  # Keep multiplying while 'original' exists in 'nums'
            original *= 2  # Multiply by 2 (assuming doubling is intended)
        return original