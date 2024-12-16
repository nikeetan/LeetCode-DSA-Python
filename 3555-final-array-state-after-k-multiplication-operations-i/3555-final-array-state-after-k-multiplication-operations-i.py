class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        i=0
        j=[x for x in nums]
        heapq.heapify(j)
        i=0
        while i<k:
            nums[nums.index(j[0])]=nums[nums.index(j[0])]*multiplier
            j[0]=j[0]*multiplier
            heapq.heapify(j)
            i+=1
        return nums




