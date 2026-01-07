class Solution:
    def average(self, salary: List[int]) -> float:
        salary.pop(salary.index(min(salary)))
        salary.pop(salary.index(max(salary)))
        avg = sum(salary)/len(salary)

        return avg