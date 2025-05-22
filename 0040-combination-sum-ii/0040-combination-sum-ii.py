class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def helper(indx, total, curr):
            if indx >= len(candidates) and total != target:
                return
            if total == target:
                res.append(curr[:])
                return
            
            for i in range(indx, len(candidates)):
                if total + candidates[i] > target:
                    return
                if i > indx  and candidates[i -1] == candidates[i]:
                    continue
                curr.append(candidates[i])
                helper(i + 1, total + candidates[i], curr)
                curr.pop()
        helper(0, 0, [])
        return res