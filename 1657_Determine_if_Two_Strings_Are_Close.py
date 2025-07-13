class Solution(object):
    def closeStrings(self, word1, word2):
        set1 = set(word1)
        set2 = set(word2)

        if set1 != set2:
            return False
        
        counts1 = {}
        counts2 = {}
        
        for c in set1:
            count = word1.count(c)
            counts1[count] = counts1.get(count, 0) + 1
        
        for c in set2:
            count = word2.count(c)
            counts2[count] = counts2.get(count, 0) + 1
        
        if counts1 != counts2:
            return False

        return True