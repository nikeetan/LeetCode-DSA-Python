class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sort to group duplicates
        
        def backtrack(indx, path):
            res.append(path[:])  # Append a copy of path
            
            for i in range(indx, len(nums)):
                # Skip duplicates at the same tree level
                if i > indx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Backtrack

        backtrack(0, [])
        return res