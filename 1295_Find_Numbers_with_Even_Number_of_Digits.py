class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for num in nums:
            # Convert the number to a string and count its length
            num_digits = len(str(num))
            
            # Check if the number of digits is even
            if num_digits % 2 == 0:
                count += 1
        
        return count