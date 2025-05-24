class Solution(object):
    def leftRightDifference(self, nums):
        n = len(nums)
        answer = []
        total_sum = sum(nums)
        left_sum = 0
        
        for i in range(n):
            # Right sum = total_sum - left_sum - nums[i]
            right_sum = total_sum - left_sum - nums[i]
            
            # Calculate absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # Update left_sum for next iteration
            left_sum += nums[i]
        
        return answer