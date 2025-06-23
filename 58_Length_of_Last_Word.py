class Solution:
    def lengthOfLastWord(self, s):
        s=s.strip()
        s=s.split()
        w=s[-1]
        return len(w)