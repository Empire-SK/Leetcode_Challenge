class Solution(object):
    def finalValueAfterOperations(self, operations):
        return sum(1 if op in ("++X", "X++") else -1 for op in operations)