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
    
        cnt = 0
        for i in range(1, len(filtered) - 1):
            if filtered[i] > filtered[i - 1] and filtered[i] > filtered[i + 1]:
                cnt += 1
            elif filtered[i] < filtered[i - 1] and filtered[i] < filtered[i + 1]:
                cnt += 1 
        return cnt
        #'''
# TC : O(N )