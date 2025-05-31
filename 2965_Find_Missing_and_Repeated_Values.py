class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        count = [0] * (n * n + 1)  # Array to store occurrences of each number
        repeated, missing = -1, -1

        # Count occurrences of each number in the grid
        for row in grid:
            for num in row:
                count[num] += 1

        # Identify the repeated and missing numbers
        for i in range(1, n * n + 1):
            if count[i] == 2:
                repeated = i
            elif count[i] == 0:
                missing = i

        return [repeated, missing]