from collections import Counter

class Solution(object):
    def minSteps(self, s, t):
        count_s = Counter(s)
        count_t = Counter(t)
        
        steps = 0
        for char in count_s:
            steps += max(0, count_s[char] - count_t.get(char, 0))
        
        return steps