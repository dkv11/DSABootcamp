class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)<2:
            return True
        inc = dec = True
        
        for x in range(0,len(nums)-1):
            if (nums[x+1] > nums[x]):
                dec = False
            if (nums[x+1]< nums[x]):
                inc = False
        return inc or dec
        
        