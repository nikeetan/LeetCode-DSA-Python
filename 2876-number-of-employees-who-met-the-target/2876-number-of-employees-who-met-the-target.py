class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        x= [x for x in hours if x >=target]
        return len(x)
