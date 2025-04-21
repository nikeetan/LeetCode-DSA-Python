class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # find the break point
        break_indx = -1
        for i in range(len(nums) -2 , -1 , -1):
            if nums[i] < nums[i + 1]:
                break_indx = i
                break

        if break_indx == -1:
            p1 , p2 = 0, len(nums)-1
            while p1 < p2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
                p2 -= 1
            print(nums)
        else:            
            # find the element which is just greater than the breakpoint and swap
            for i in range(len(nums)-1, -1, -1):
                if nums[i] > nums[break_indx]:
                    nums[i], nums[break_indx] = nums[break_indx], nums[i]
                    break
            
            # Rearrange
            print("break_indx", break_indx)
            if break_indx != -1:
                p1, p2 = break_indx + 1, len(nums) - 1
                while p1 < p2:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                    p2 -= 1
