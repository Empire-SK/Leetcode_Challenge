class Solution(object):
    def findErrorNums(self, nums):
        n = len(nums)
        exp_sum = n*(n+1)//2
        act_sum = sum(nums)
        duplicate = act_sum - sum(set(nums))
        m = exp_sum - (act_sum - duplicate)
        return [duplicate, m]