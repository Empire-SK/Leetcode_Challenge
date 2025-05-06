class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (high + low) // 2
            
            # If target is found, return its index
            if nums[mid] == target:
                return mid
                
            # If target is greater, ignore left half
            elif nums[mid] < target:
                low = mid + 1
                
            # If target is smaller, ignore right half
            else:
                high = mid - 1
                
        # If target wasn't found, 'low' will be the correct insertion position
        return low