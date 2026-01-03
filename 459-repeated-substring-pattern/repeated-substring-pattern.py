class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        buf = []
        for x in range(1,len(s)):
            if len(s)%x==0:
                buf.append(x)
        for i in buf:
            if (s[:i] * (len(s)//i)) == s:
                return True
            
        return False


             
        