'''
should i think of considering first element and not considering the last
ans also starying from 1st index and considering the last

[-2,4,-5,4,-5,9,4]

'''

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            # fetching the minimum
            currMin = minSub = nums[0]
            currMax = maxSub = nums[0]
            total = nums[0]
            for i in range(1, len(nums)):
                total += nums[i]
                currMin = min(currMin + nums[i], nums[i])
                currMax = max(currMax + nums[i], nums[i])
                minSub = min(currMin, minSub)
                maxSub = max(currMax, maxSub)
            
            if maxSub > 0:
                return max(maxSub, total - minSub)
            else:
                return maxSub
            