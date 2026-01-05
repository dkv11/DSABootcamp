class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <2:
            return True
        arr = sorted(arr)
        
        d = arr[1] - arr[0]
        for x in range(1,len(arr)-1):
            if (arr[x+1]-arr[x]) != d:
                return False
        
        return True