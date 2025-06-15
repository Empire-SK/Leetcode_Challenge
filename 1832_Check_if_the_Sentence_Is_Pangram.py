from collections import Counter
class Solution(object):
    def checkIfPangram(self, sentence):
        ch = Counter(sentence)
        count = len(ch)
        if count == 26:
            return True
        return False
