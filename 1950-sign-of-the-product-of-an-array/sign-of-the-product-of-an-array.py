class Solution:
    def arraySign(self, nums: List[int]) -> int:
        x = 0
        product = 1
        for x in nums:
            product = x *product
        if product > 0:
            result = 1
        elif product < 0 :
            result = -1
        else :
            result = 0
        return result 
