class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        target = 0
        for p1 in range(len(nums) - 2):
            p2 = p1 + 1
            p3 = len(nums) - 1
            while p2 < p3:
                if (nums[p1] + nums[p2] + nums[p3]) == target:
                    res.add((nums[p1], nums[p2], nums[p3]))
                    p2 += 1 
                elif nums[p2] + nums[p3] < (target - nums[p1]):
                    p2 += 1
                else:
                    p3 -= 1
        return list(res)
'''
nums = [-1,0,1,2,-1,-4] 

nums = [ -4, -1, -1 , 0 , 1, 2]   
         p1  p2              p3
             p1           p2
                          p3
                 p1       p2  
                          p3
                     p1   p2 p3    



res = [[-1, -1, 2], 
'''