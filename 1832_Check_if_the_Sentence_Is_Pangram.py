class Solution(object):
    def checkIfPangram(self, sentence):
        s = list(set(list(sentence)))
        if len(s) == 26:
            return True
        return False
