class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr_indx = 1
        max_diff = float('-inf')
        prev_min = nums[0]
        while curr_indx < len(nums):
            if nums[curr_indx] < nums[curr_indx - 1]:
                if nums[curr_indx] < prev_min:
                    prev_min = nums[curr_indx]
            elif nums[curr_indx] > nums[curr_indx - 1]:
                max_diff = max(max_diff, nums[curr_indx] - nums[curr_indx - 1], nums[curr_indx] - prev_min)
            curr_indx += 1
        return max_diff if max_diff != float('-inf') else -1