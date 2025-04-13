'''
i = 0 , len(nums)

i +1  , (len(nums) + (i + 1))
i% len(nums) and (i + 1)% l
'''

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):    
            flag = 0                  
            for j in range(i+1 , (len(nums)+ (i+1))):   
                if nums [ i% len(nums)] < nums [j % len(nums)]:
                    res.append(nums[j%len(nums)])                  
                    flag = 1 
                    break
            if flag == 0:
                res.append(-1)
        return res

        