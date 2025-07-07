from collections import Counter
class Solution(object):
    def mostFrequentEven(self, nums):
        even_nums = [num for num in nums if num % 2 == 0]
        if not even_nums:
            return -1
        freq = Counter(even_nums)
        # Find the number with highest frequency, break ties by choosing the smallest number
        return min(freq.items(), key=lambda x: (-x[1], x[0]))[0]
