from collections import Counter;
class Solution:
    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2): return self.intersect(nums2, nums1)
            
        cnt = Counter(nums1)
        ans = []
        for x in nums2:
            if cnt[x] > 0:
                ans.append(x)
                cnt[x] -= 1
        return ans