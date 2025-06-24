class Solution(object):
    def duplicateZeros(self, arr):
        dupes = 0
        n = len(arr)
        currLen = n-1

        for i in range(currLen + 1):
            if i > currLen - dupes:
                break
            
            if arr[i] == 0:
                if i == currLen - dupes:
                    arr[currLen] = 0
                    currLen -= 1
                    break
                dupes += 1
        
        last = currLen - dupes

        for j in range(last,-1,-1):
            if arr[j] == 0:
                arr[j+dupes] = 0
                dupes -= 1
                arr[j+dupes] = 0
            else:
                arr[j+dupes] = arr[j]