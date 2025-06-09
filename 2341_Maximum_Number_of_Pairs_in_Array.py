from collections import Counter

class Solution(object):
    def numberOfPairs(self, nums):
        freq = Counter(nums)  # Count occurrences of each number
        pairs = sum(v // 2 for v in freq.values())  # Calculate total pairs
        leftovers = sum(v % 2 for v in freq.values())  # Count remaining elements
        return [pairs, leftovers]
