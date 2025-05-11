class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        # Map the ruleKey to its corresponding index in each item array
        key_index = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        # Get the appropriate index for the given ruleKey
        index = key_index[ruleKey]
        
        # Count items where the value at the determined index matches ruleValue
        count = 0
        for item in items:
            if item[index] == ruleValue:
                count += 1
                
        return count