## https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        avg = sum(salary) - (max(salary)+min(salary))
        return avg/(len(salary)-2)