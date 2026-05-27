class Solution(object):
    def checkInclusion(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        s1_counts = [0]*26
        s2_counts = [0]*26
        
        for r in range(n1):
            s1_counts[ord(s1[r])-97] +=1   #for lower in n1
            s2_counts[ord(s2[r])-97] +=1   #for lower in n1

        #now again checking if count in s1 and s2 are same:
        if s1_counts == s2_counts:
            return True
        
        for r in range(n1,n2):
            s2_counts[ord(s2[r])-97] +=1
            s2_counts[ord(s2[r-n1])-97] -=1
            if s1_counts == s2_counts:
                return True

        return False