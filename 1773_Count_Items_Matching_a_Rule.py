class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count = 0
        for i in range(0, len(items)):
            current_list = items[i]
            if ruleKey == "type" and ruleValue == current_list[0]:
                count += 1
            elif ruleKey == "color" and ruleValue == current_list[1]: 
                count += 1
            elif ruleKey == "name" and ruleValue == current_list[2]:
                count += 1
        return count 