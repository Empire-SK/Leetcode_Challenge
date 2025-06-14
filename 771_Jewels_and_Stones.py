class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)  # Convert jewels to a set for fast lookup
        return sum(stone in jewel_set for stone in stones)