class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        target = 0
        for p1 in range(len(nums) - 2):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            p2 = p1 + 1
            p3 = len(nums) - 1
            while p2 < p3:
                if (nums[p1] + nums[p2] + nums[p3]) == target:
                    res.append((nums[p1], nums[p2], nums[p3]))
                    while p2 < p3 and (nums[p2] == nums[p2 + 1]):
                        p2 += 1
                    while nums[p3] == nums[p3 - 1] and p3 > p2:
                        p3 -= 1
                    p2 += 1
                    p3 -= 1 
                elif nums[p2] + nums[p3] < (target - nums[p1]):
                    p2 += 1  
                else:
                    p3 -= 1
        return res
