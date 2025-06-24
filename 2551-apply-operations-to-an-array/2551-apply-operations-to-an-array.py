class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for j in range(len(nums) - 1):
            if nums[j] != nums[j + 1]:
                continue
            else:
                nums[j] = 2 * nums[j]
                nums[j + 1] = 0
        print(nums)
        # Move zeroes towards the end
        p1, p2 = 0, 1
        while p2 < len(nums):
            if nums[p1] == 0:
                while p2 < len(nums) and nums[p2] == 0:
                    p2 += 1
                if p2 < len(nums):
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 = p1 + 1
                p2 = p2 + 1
                continue
            p1 += 1
            p2 += 1
        return nums
            