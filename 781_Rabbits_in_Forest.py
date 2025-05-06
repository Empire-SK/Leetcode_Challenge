class Solution(object):
    def numRabbits(self, answers):
        count = {}
        for ans in answers:
            count[ans] = count.get(ans, 0) + 1
        
        total_rabbits = 0
        
        for ans, frequency in count.items():
            complete_groups = (frequency // (ans + 1))
            partial_group = 1 if frequency % (ans + 1) > 0 else 0
            
            total_rabbits += (complete_groups + partial_group) * (ans + 1)
        
        return total_rabbits