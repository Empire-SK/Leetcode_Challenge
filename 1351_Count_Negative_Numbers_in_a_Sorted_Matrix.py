class Solution(object):
    def countNegatives(self, grid):
        count = 0
        m, n = len(grid), len(grid[0])
        
        for row in grid:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid - 1  # Search earlier elements
                else:
                    left = mid + 1  # Search later elements
            count += n - left  # 'left' is the first negative index in the row
        
        return count