class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curr_indx = 1
        max_diff = float('-inf')
        while curr_indx < len(nums):
            if nums[curr_indx] < nums[curr_indx - 1]:
                curr_indx += 1
                continue
            else:
                prev_indx = curr_indx - 1
                while prev_indx >= 0 and nums[curr_indx] > nums[prev_indx]:
                    max_diff = max(max_diff, nums[curr_indx] - nums[prev_indx])
                    prev_indx -= 1
            curr_indx += 1
        return max_diff if max_diff != float('-inf') else -1