class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        res = []
        def helper(indx, sl):
            if indx >= size:
                res.append(sl[:])
                return 
            sl.append(nums[indx])
            helper(indx + 1, sl)
            sl.pop()
            helper(indx + 1, sl)

        helper(0, [])
        return res