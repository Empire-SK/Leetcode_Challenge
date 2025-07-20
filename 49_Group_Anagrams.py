from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Sort the word and use it as a key
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())