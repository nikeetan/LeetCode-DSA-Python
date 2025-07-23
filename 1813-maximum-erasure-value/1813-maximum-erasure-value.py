'''
    [4, 2,  4,  5,  6]


'''

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        numberMap = defaultdict(int)
        left, right = 0, 0
        maxLen = float('-inf')
        maxSum = float('-inf')
        currSum = 0
        while right < len(nums):
            currnum = nums[right]
            while currnum in numberMap:
                if numberMap[nums[left]] - 1 == 0:
                    del numberMap[nums[left]]
                else:
                    numberMap[nums[left]] -= 1
                currSum -= nums[left]
                left += 1
            numberMap[currnum] += 1
            currSum += currnum
            maxSum = max(maxSum, currSum)
            right += 1
        return maxSum
                
