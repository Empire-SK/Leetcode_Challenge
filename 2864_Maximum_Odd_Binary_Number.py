class Solution(object):
    def maximumOddBinaryNumber(self, s):

        # Count the number of '1's in the string
        count_ones = s.count('1')
        
        # Calculate the number of '0's
        count_zeros = len(s) - count_ones
        
        # To make the maximum odd binary number:
        # 1. We need one '1' at the end to make it odd
        # 2. We place all remaining '1's at the beginning
        # 3. We place all '0's in the middle
        
        # Construct the result: (count_ones-1) '1's, followed by count_zeros '0's, followed by a '1'
        result = '1' * (count_ones - 1) + '0' * count_zeros + '1'
        
        return result