class Solution(object):
    def minSteps(self, s, t):
        set_s = list(set(s))
        set_t = list(set(t))
        steps = 0
        for i in set_s:
            if i not in set_t:
                steps += s.count(i)
            else:
                steps += abs(s.count(i) - t.count(i))
        for i in set_t:
            if i not in set_s:
                steps += t.count(i)
        return steps
        