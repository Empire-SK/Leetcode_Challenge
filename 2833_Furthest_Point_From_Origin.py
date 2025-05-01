class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        # Count the fixed moves
        r_count = moves.count('R')
        l_count = moves.count('L')
        wildcard_count = moves.count('_')
        
        # Calculate the net fixed direction
        net_fixed = r_count - l_count
        
        # Calculate maximum possible distance in each direction
        # If all wildcards go right: net_fixed + wildcard_count
        # If all wildcards go left: net_fixed - wildcard_count
        right_distance = net_fixed + wildcard_count
        left_distance = net_fixed - wildcard_count
        
        # The furthest point is the maximum absolute distance
        return max(abs(right_distance), abs(left_distance))