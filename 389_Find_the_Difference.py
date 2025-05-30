class Solution(object):
    def findTheDifference(self, s, t):
        result = 0
        for char in s + t:  
            result ^= ord(char)  # XOR all characters
        return chr(result)  # Convert back to a character