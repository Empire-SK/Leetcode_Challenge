class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        counts=[0]*26
        countt=[0]*26
        for i in range(len(s)):
            counts[ord(s[i])-ord('a')]+=1
            countt[ord(t[i])-ord('a')]+=1
        return counts==countt     