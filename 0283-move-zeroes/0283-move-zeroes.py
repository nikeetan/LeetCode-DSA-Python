class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        else:
            fp , sp = 0 , 1
            while sp < len(nums):
                if (nums[fp] == 0) and (nums[sp] != 0):
                    nums[fp], nums[sp] = nums[sp], nums[fp]
                    fp += 1
                elif (nums[fp] != 0) and (nums[sp] == 0):
                    fp = sp
                sp += 1
            return nums
