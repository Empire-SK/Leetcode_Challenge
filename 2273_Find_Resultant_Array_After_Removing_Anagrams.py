class Solution(object):
    def removeAnagrams(self, words):
        result = []
        
        for word in words:
            # If result is empty or the last word in result isn't an anagram of current word it will be added
            if not result or sorted(word) != sorted(result[-1]):
                result.append(word)
        
        return result