class Solution(object):
    def commonFactors(self, a, b):
        count = 0
        
        if a < b:
            minimum = a
        else:
            minimum = b
            
        for x in range(1, minimum + 1):
            if a % x == 0 and b % x == 0:
                count += 1
                
        return count