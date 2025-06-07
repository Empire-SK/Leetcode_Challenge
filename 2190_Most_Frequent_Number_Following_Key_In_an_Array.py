class Solution(object):
    def mostFrequent(self, nums, key):

        lookup = dict()
        max_ele = None
        max_count = -float("inf")
        for i in range(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] in lookup:
                    lookup[nums[i+1]] += 1
                else:
                    lookup[nums[i+1]] = 0
                if lookup[nums[i+1]] > max_count:
                    max_count = lookup[nums[i+1]]
                    max_ele = nums[i+1]
        return max_ele
        