'''
again i can think of bfs herr
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        jumps = 0
        far = float('-inf')
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                jumps += 1
                end = far
        return jumps
        