class Solution(object):
    def isAcronym(self, words, s):
        l=[]
        for num in words:
            l.append(num[0])
        if "".join(l)==s:
            return True
        return False