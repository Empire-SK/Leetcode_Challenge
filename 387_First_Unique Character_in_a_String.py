from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        freq_map = Counter(s)  # Efficient frequency count
        for i, char in enumerate(s):  # Iterate through the string
            if freq_map[char] == 1:
                return i
        return -1  # No unique character found
