class Solution:
    def getSecondLargest(self, arr):
        largest = float("-inf")
        S_largest = float("-inf")
        
        for i in arr:
            if i > largest:
                S_largest = largest
                largest = i
            elif i > S_largest and not(i >= largest):
                S_largest = i
                
        
        if S_largest == float("-inf"):
            return -1
        else:
            return S_largest