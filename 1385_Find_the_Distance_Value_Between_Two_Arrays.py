class Solution(object):
    def findClosestDiff(self, element, arr, d):
        l, h = 0, len(arr) - 1
        
        while l <= h:
            mid = (l + h) // 2
            
            if abs(element - arr[mid]) <= d:
                return False
            elif arr[mid] < element:
                l = mid + 1
            elif arr[mid] > element:
                h = mid - 1
        return True

    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        dis_value = 0
        
        for element in arr1:
            if self.findClosestDiff(element, arr2, d):
                dis_value += 1
            
        return dis_value 