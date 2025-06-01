'''
hills set 

'''

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        filtered = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            filtered.append(nums[i])
        
        
        hillset = set()
        valleyset = set()

        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                hillset.add((i - 1, i + 1))
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                valleyset.add((i - 1, i + 1))
        return len(hillset) + len(valleyset)
        #'''
# TC : O(N )