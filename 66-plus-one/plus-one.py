class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringdigit = ""
        for digit in digits:
            digit = str(digit)
            stringdigit = stringdigit + digit

        num= str(int(stringdigit)+1)
        num = list(map(int,num))
        
        return num

        