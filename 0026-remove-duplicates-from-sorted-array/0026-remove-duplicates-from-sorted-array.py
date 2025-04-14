'''
fp     sp 
[0, 0,  1, 1, 1, 1, 2, 2, 3, 3, 4]
    fp             sp
[0, 1,  0, 1, 1, 1, 2, 2, 3, 3, 4]
        fp                sp
[0, 1,  2, 1, 1, 1, 0, 2, 3, 3, 4]
             fp                  
[0, 1,  2, 3, 4, 1, 0, 2, 1, 3, 1]


[1, 1, 2]
if len(nums) <= 1: 
    return nums
else:                                 
    fp , sp = 0 , 1                 
    while sp < len(nums):

        # not equal condition
        if nums [fp] != nums[sp]:
            nums [fp + 1] , nums [sp] = nums [sp], nums [fp]
            fp = fp + 1
        sp += 1

TC : o(n)
SC : o(1)

[1, 2, 1] 
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 1
        else:                                 
            fp , sp = 0 , 1     #[0 , 1]            
            while sp < len(nums):
                # not equal condition
                if nums [fp] != nums[sp]:       
                    nums [fp + 1] = nums [sp]
                    fp = fp + 1
                sp += 1
            return fp + 1 

