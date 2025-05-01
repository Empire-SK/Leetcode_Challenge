class Solution(object):
    def isThree(self, n):
        count=0
        for x in range(1,n+1):
          if n % x == 0:
            count+=1
        return count == 3  