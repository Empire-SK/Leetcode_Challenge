class Solution(object):
    def alternateDigitSum(self, n):
        # Convert n to string to process digits from left to right
        digits = str(n)
        result = 0
        sign = 1
        
        # Process each digit from left to right
        for digit in digits:
            result += int(digit) * sign
            sign *= -1  # Flip the sign for the next digit
            
        return result