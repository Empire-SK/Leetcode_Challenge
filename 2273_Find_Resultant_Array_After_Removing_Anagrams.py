class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        right = 1
        left = right - 1
        while right < len(words):
            left_word = words[left]
            right_word = words[right]
            if sorted(left_word) == sorted(right_word):
                words.remove(right_word)
            else:
                right += 1
                left = right - 1
        return words