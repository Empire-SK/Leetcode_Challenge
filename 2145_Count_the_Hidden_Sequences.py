class Solution(object):
    def numberOfArrays(self, differences, lower, upper):
        # Start with offset 0 (representing hidden[0])
        current_offset = 0
        min_offset = 0
        max_offset = 0
        
        # Calculate the min and max offsets from the starting value
        for diff in differences:
            current_offset += diff
            min_offset = min(min_offset, current_offset)
            max_offset = max(max_offset, current_offset)
        
        # Calculate valid range for starting value
        # hidden[0] + min_offset >= lower → hidden[0] >= lower - min_offset
        # hidden[0] + max_offset <= upper → hidden[0] <= upper - max_offset
        valid_start_min = lower - min_offset
        valid_start_max = upper - max_offset
        
        # Count valid starting values
        valid_starts = valid_start_max - valid_start_min + 1
        return max(0, valid_starts)