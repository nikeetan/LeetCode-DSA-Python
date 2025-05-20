class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        i can think of using cyclic sort if the numbers are in the range[1, n ] after sorting i will check whether the curr_indx element is placed if it's not then the number which is present at the index is my repeated number
        '''
        indx = 0
        while indx < len(nums):
            val = nums[indx] - 1
            if nums[indx] != nums[val]:
                nums[indx], nums[val] = nums[val], nums[indx]
            else:
                indx += 1     
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res