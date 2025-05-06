class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        from collections import defaultdict
        
        count = defaultdict(int)
        pairs = 0
        
        for a, b in dominoes:
            key = (min(a, b), max(a, b))  # Normalize representation
            pairs += count[key]  # Add previous occurrences to count of pairs if previous one match with current
            count[key] += 1  # Update count for future matches
        
        return pairs