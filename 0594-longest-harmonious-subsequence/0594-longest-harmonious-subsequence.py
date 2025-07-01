'''
generate all subsequence and traverse each subsequence to find the difference whether they are 1 if yes then record the length in  a variable maximum and always it will be a max(curr_maximum , new_subseqlen)
'''

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numMap = {}
        for i in nums:
            if i not in numMap:
                numMap[i] = 1
            else:
                numMap[i] += 1
        nums.sort()

        # two pointers
        firstPointer, secondPointer = 0, 1
        subseqLen = 0
        while secondPointer < len(nums):
            if nums[secondPointer] - nums[firstPointer] == 1:
                subseqLen = max(subseqLen, numMap[nums[firstPointer]] + numMap[nums[secondPointer]])
            firstPointer += 1
            secondPointer += 1
        return subseqLen
'''
test case
[1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2]

numMap = {1 : 1 , 2 : 3, 3 : 2, 5 : 1, 7 : 1}
[1, 2,  2,  2,  3,  3,  5,  7]
                        fp  sp
subseqLen = 5

'''