class Solution(object):
    def capitalizeTitle(self, title):
        return " ".join(word.lower() if len(word) <= 2 else word.capitalize() for word in title.split())