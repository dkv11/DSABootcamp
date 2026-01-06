class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        output = s.split()

        return len(output[-1])