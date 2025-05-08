import math
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        else:
            exp = 1
            while max(nums) // exp > 0:
                num_map = {i : [] for i in range(10)}
                for num in nums:
                    num_map[(num // exp) % 10].append(num)
                exp = exp * 10
                curr_indx = 0
                for key , val in num_map.items():
                    for i in range(len(val)):
                        nums[curr_indx] = val[i]
                        curr_indx += 1 

            '''
            max_Gap
            '''
            maxi = float('-inf')
            for i in range(1, len(nums)):
                if nums[i] - nums[i - 1] > maxi:
                    maxi = nums[i] - nums[i -1]
    
            return maxi


    # TC : O(n logn) for sorting and then for traversing to find the maximum difference it's o(n)
    # SC : O(1)