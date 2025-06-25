class Solution(object):
    def intersection(self, nums1, nums2):
        r=set(nums1).intersection(set(nums2))
        return  list(r)