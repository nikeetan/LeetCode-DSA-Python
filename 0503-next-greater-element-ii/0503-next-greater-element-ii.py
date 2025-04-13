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
        indx = len(nums) - 1
        stack = []
        res = [-1] * len(nums)

        # pass 1                    [1, 2, 1]
        while indx >= 0:                # 0        

            while stack and nums[indx] >= stack[-1]: # [2] 1 > 2
                stack.pop()
            
            if stack:                   
                res[indx] = stack[-1]           #[2, -1, -1]
            stack.append(nums[indx])            #[2, 1]        
            indx -= 1

        # pass 2
        indx = len(nums) - 1                # 1
        while indx >= 0:                    # 2 > 0

            while stack and nums[indx] >= stack[-1]:  # [2] 
                stack.pop()                             
            
            if stack:                           
                res[indx] = stack[-1]           #[2, -1 , 2]
            stack.append(nums[indx])            #[2, 1]
            indx -= 1
        return res
        
                
                


