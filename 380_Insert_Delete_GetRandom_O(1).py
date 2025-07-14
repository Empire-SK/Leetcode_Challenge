import random

class RandomizedSet(object):
    def __init__(self):
        self.nums = []  # List to store the actual values
        self.indices = {}  # Dictionary to map value -> index in nums
        
    def insert(self, val):
        if val in self.indices:
            return False
        
        # Add the value to the end of the list
        self.nums.append(val)
        # Map the value to its index in the list
        self.indices[val] = len(self.nums) - 1
        return True
        
    def remove(self, val):
        if val not in self.indices:
            return False
        
        # Get the index of the value to remove
        index_to_remove = self.indices[val]
        last_element = self.nums[-1]
        
        # Move the last element to the position of the element to remove
        self.nums[index_to_remove] = last_element
        self.indices[last_element] = index_to_remove
        
        # Remove the last element from the list and the mapping
        self.nums.pop()
        del self.indices[val]
        
        return True
        
    def getRandom(self):
        return random.choice(self.nums)