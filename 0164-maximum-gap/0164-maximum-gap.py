class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        else:
            nums.sort()
            curr_indx = 1
            maxi = float('-inf')
            while curr_indx < len(nums):
                if nums[curr_indx] - nums[curr_indx - 1] > maxi:
                    maxi = nums[curr_indx] - nums[curr_indx - 1]
                curr_indx += 1
            return maxi
    # TC : O(n logn) for sorting and then for traversing to find the maximum difference it's o(n)
    # SC : O(1)