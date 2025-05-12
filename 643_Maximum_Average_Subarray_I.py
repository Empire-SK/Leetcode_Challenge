class Solution(object):
    def findMaxAverage(self, nums, k):
        r = sum(nums[:k])  # Compute sum of the first 'k' elements
        s = 1  # Start index of the sliding window
        m = r  # Initialize max sum with the sum of the first 'k' elements
        e = k  # End index of the sliding window
        
        while e < len(nums):
            r += nums[e] - nums[s - 1]  # Update sum by adding new element and removing the outgoing one
            if m < r:
                m = r  # Update max sum if new sum is greater
            e += 1  # Move the window forward
            s += 1  # Move the start index forward
            
        return m / float(k)  # Return the maximum average