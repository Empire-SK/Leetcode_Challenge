class Solution(object):
    def maximumLengthSubstring(self, s):
        from collections import defaultdict
        
        freq = defaultdict(int)
        l, max_length = 0, 0
        
        for r in range(len(s)):
            freq[s[r]] += 1
            
            while any(v > 2 for v in freq.values()):
                freq[s[l]] -= 1
                l += 1
            
            max_length = max(max_length, r - l + 1)
        
        return max_length