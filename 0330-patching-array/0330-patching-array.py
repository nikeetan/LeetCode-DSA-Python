class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        miss = 1
        indx = 0
        while miss <= n:
            print(miss)
            if (indx < len(nums)) and  (nums[indx]<= miss):
                miss += nums[indx]
                indx += 1
            else:
                miss += miss
                patches += 1
        return patches


