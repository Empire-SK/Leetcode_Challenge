class Solution(object):
    def findMaxAverage(self, nums, k):
        # Calculate initial sum of first k elements
        current_sum = sum(nums[:k])
        
        # Initialize max_sum with the sum of first window
        max_sum = current_sum
        
        # Slide the window and update max_sum
        for i in range(k, len(nums)):
            # Add the next element and remove the first element of previous window
            current_sum = current_sum + nums[i] - nums[i - k]
            # Update max_sum if current_sum is greater
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum average
        return max_sum / float(k)