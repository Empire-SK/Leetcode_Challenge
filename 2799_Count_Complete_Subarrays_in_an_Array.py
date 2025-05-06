class Solution(object):
    def countCompleteSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Get the number of distinct elements in the original array
        distinct_elements = len(set(nums))
        n = len(nums)
        count = 0
        
        # Check each possible subarray
        for start in range(n):
            # Use a set to track distinct elements in the current subarray
            current_distinct = set()
            for end in range(start, n):
                # Add the current element to our set
                current_distinct.add(nums[end])
                
                # If the subarray has the same number of distinct elements as the full array,
                # it's a complete subarray
                if len(current_distinct) == distinct_elements:
                    count += 1
                    
        return count