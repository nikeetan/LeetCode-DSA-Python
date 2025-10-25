class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        # using base condition
        res_stk = []
        
        def helper(indx, stk):

            if indx == len(nums):
                res_stk.append(stk[:])
                return
            
            helper(indx + 1, stk + [nums[indx]])
            helper(indx + 1, stk)

        helper(0, [])
        return res_stk
        
        
    
find_subsets = Solution()
array = [1, 2, 3]
print(find_subsets.subsets(array))
