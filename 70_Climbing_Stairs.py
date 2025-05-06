class Solution(object):
    def climbStairs(self, n):
          # Base cases
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
            
        # Initialize first two values in the sequence
        first, second = 1, 2
        
        # Calculate the nth value using bottom-up approach
        for i in range(3, n + 1):
            curr = first + second
            first = second
            second = curr
            
        return second