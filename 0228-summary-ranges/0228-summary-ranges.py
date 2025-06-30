'''
if they are consecutive i can have the range till the difference between currelement and next element > 1 
and whenver the curr_element is greater than the next element by more than 1 then there will the range of itself included

I need two pointer approach
TC - > O(n)
SC -> o(n)
'''

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return nums
        else:
            firstPointer, secondPointer = 0, 1
            start = -1
            rangeArray = []
            while secondPointer < len(nums):
                if abs(nums[secondPointer] - nums[firstPointer]) == 1:
                    if start == -1:
                        start = firstPointer
                elif nums[secondPointer] - nums[firstPointer] > 1:
                    if (start > -1):
                        rangeString = str(nums[start]) + '->' + str(nums[firstPointer])
                        rangeArray.append(rangeString)
                        start = -1
                    else:
                        rangeArray.append(str(nums[firstPointer]))
                firstPointer += 1
                secondPointer += 1
            if start != -1:
                rangeString = str(nums[start]) + '->' + str(nums[firstPointer])
                rangeArray.append(rangeString)
            else:
                rangeArray.append(str(nums[firstPointer]))
            return rangeArray


                


        