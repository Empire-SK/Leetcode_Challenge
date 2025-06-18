class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        total = n * n
        
        # Compute actual sum and sum of squares from grid
        actual_sum = 0
        actual_sum_squares = 0
        for row in grid:
            for num in row:
                actual_sum += num
                actual_sum_squares += num * num
        
        # Expected sum and sum of squares from 1 to n²
        expected_sum = (total * (total + 1)) // 2
        expected_sum_squares = (total * (total + 1) * (2 * total + 1)) // 6
        
        # Differences:
        # actual_sum = expected_sum - missing + repeated => diff_sum = repeated - missing
        # actual_sum_squares = expected_sum_squares - missing² + repeated²
        diff_sum = actual_sum - expected_sum  # = repeated - missing (corrected)
        diff_squares = actual_sum_squares - expected_sum_squares  # = repeated² - missing²
        
        # diff_squares = (repeated - missing)(repeated + missing)
        # Thus, repeated + missing = diff_squares // diff_sum
        # Note: diff_sum ≠ 0 since repeated ≠ missing (per constraints)
        sum_rm = diff_squares // diff_sum
        
        # Solve:
        # repeated - missing = diff_sum
        # repeated + missing = sum_rm
        repeated = (diff_sum + sum_rm) // 2
        missing = sum_rm - repeated
        
        return [repeated, missing]