'''
i = 0 , len(nums)

i +1  , (len(nums) + (i + 1))
i% len(nums) and (i + 1)% l
'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        '''
        first pass
        '''
        indx = (len(nums) - 1) * 2
        stack = []
        res = [-1] * len(nums)

        # pass 1                    [1, 2, 1]
        while indx >= 0:                # 0        
            curr_ind = indx % len(nums)
            while stack and nums[curr_ind] >= stack[-1]: # [2] 1 > 2
                stack.pop()
            
            if stack:                   
                res[curr_ind] = stack[-1]           #[2, -1, -1]
            stack.append(nums[curr_ind])            #[2, 1]        
            indx -= 1

        return res
        
                
                


