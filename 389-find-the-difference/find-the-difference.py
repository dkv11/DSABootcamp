class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        
        for ch in t:
            freq[ch] = freq.get(ch,0) - 1
            if freq.get(ch) <0:
                return ch
        



               
            

