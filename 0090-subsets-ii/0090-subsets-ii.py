class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()  
        
        def backtrack(indx):
            res.append(path[:])  # Append a copy of path
            
            for i in range(indx, len(nums)):
               
                if i > indx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()  # Backtrack

        backtrack(0)
        return res