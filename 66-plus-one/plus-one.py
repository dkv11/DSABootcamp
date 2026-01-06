class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            digits[-1]=digits[-1]+1
            return digits
        result = int("".join(map(str, digits)))

        result = result+1
        new_list = list(map(int, str(result)))
        return new_list

        