class Solution:
    def countDigits(self, num: int) -> int:
        n=num
        c=0        
        while n>0:
            last_digit= n%10
            if num%last_digit==0:
                c=c+1
            n=n//10
        return c
        