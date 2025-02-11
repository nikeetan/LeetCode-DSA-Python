class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        x=[x for x in nums if x!=0]
        if x is None:
            return 0
        else:
            similar_count=len(x)-len(set(x))
            return len(x)-similar_count