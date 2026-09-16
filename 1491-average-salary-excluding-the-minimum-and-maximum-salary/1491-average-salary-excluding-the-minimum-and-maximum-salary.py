class Solution:
    def average(self, salary: List[int]) -> float:
        mini=min(salary)
        maxi=max(salary)
        salary.remove(mini)
        salary.remove(maxi)
        return sum(salary)/len(salary)
        