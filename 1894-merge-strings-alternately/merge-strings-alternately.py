class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        buf=[]
        while i < len(word1) or j < len(word2):
            if i<len(word1):
                buf.append(word1[i])
            if j<len(word2):
                buf.append(word2[j])
            i+=1
            j+=1
        buf = ''.join(buf)
        return buf