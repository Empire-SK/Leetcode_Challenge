class Solution(object):
    def getCommon(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1.intersection(set2)

        if common:
            return min(common)
        else: 
            return -1       
        