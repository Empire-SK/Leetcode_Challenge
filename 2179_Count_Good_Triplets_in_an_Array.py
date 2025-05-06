class Solution(object):
    def goodTriplets(self, nums1, nums2):
        n = len(nums1)
        
        # Create position arrays
        pos1 = [0] * n  # pos1[v] = index of value v in nums1
        pos2 = [0] * n  # pos2[v] = index of value v in nums2
        for i in range(n):
            pos1[nums1[i]] = i
            pos2[nums2[i]] = i
        
        # Fenwick Tree class
        class FenwickTree:
            def __init__(self, size):
                self.size = size
                self.tree = [0] * (size + 1)
            
            def update(self, index, delta):
                index += 1  # 1-based indexing
                while index <= self.size:
                    self.tree[index] += delta
                    index += index & (-index)
            
            def query(self, index):
                index += 1  # 1-based indexing
                total = 0
                while index > 0:
                    total += self.tree[index]
                    index -= index & (-index)
                return total
        
        # Initialize Fenwick Tree
        fenwick = FenwickTree(n)
        
        # Store values by pos1 to process in order of nums1 positions
        value_by_pos1 = sorted(range(n), key=lambda v: pos1[v])
        
        # Count elements to the right for each pos2
        right_count = [0] * n
        for v in reversed(value_by_pos1):
            right_count[v] = n - 1 - pos2[v]  # Initial count of z with pos2[z] > pos2[v]
        
        result = 0
        processed = 0  # Number of elements processed
        for v in value_by_pos1:
            y = v
            pos2_y = pos2[y]
            
            # Count x: elements with pos1[x] < pos1[y] and pos2[x] < pos2[y]
            left_count = fenwick.query(pos2_y)
            
            # Count z: elements with pos1[z] > pos1[y] and pos2[z] > pos2[y]
            right = right_count[y] - (processed - left_count)
            
            # Number of good triplets with y as middle element
            result += left_count * right
            
            # Update Fenwick Tree and processed count
            fenwick.update(pos2_y, 1)
            processed += 1
        
        return result