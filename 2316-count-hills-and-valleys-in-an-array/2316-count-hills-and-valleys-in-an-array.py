'''
hills set 

'''

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hillset = set()
        valleyset = set()

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                hillset.add((i - 1, i + 1))
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                valleyset.add((i - 1, i + 1))
            
            elif nums[i] == nums[i - 1] or nums[i] == nums[i + 1]:
                j = i
                if nums[i] == nums[i - 1]:
                    curr = nums[i]
                    while j > 0 and curr == nums[j]:
                        j -= 1
                    if j < 0:
                        continue
                    if nums[i] > nums[j] and nums[i] > nums[i + 1]:
                        hillset.add((j, i + 1))
                    elif nums[i] < nums[j] and nums[i] < nums[i + 1]:
                        valleyset.add((j, i + 1))
                else:
                    curr = nums[i]
                    while j < len(nums) and curr == nums[j]:
                        j += 1
                    if j == len(nums):
                        continue
                    if nums[i] > nums[i - 1] and nums[i] > nums[j]:
                        hillset.add((i - 1, j))
                    elif nums[i] < nums[i - 1] and nums[i] < nums[j]:
                        valleyset.add((i - 1, j))
        return len(hillset) + len(valleyset)
                        
            
        