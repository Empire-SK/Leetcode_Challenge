class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:  # Pythonic way to check palindrome
                return word
        return ""