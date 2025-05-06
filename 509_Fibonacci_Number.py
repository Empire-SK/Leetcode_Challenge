class Solution(object):
    def fib(self, n):
        if n <= 1:
            return n
        else:
            return self.fib(n - 1) + self.fib(n - 2)
        
        # This is a recursive implementation of the Fibonacci sequence.
        # Attempt 1