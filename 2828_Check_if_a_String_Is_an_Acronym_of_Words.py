class Solution(object):
    def isAcronym(self, words, s):
        return s == ''.join(word[0] for word in words)