class Solution(object):
    def restoreString(self, s, indices):
        answer = [""] * len(s)  # Create a list of empty strings
        for i in range(len(indices)):
            answer[indices[i]] = s[i]  # Place characters in correct positions
        return "".join(answer)  # Convert list to final string