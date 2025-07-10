class Solution(object):
    def minSteps(self, s, t):
        ret_val = 0
        l = list("abcdefghijklmnopqrstuvwxyz")
        for char in l:
            s_count = s.count(char)
            t_count = t.count(char)
            if s_count > t_count:
                ret_val += s_count - t_count
        return ret_val