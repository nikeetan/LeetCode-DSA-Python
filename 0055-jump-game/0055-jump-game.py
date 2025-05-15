class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # @cache
        # def helper(indx):
        #     if indx + 1 >= len(nums):
        #         return True
        #     for i in range(1, nums[indx] + 1):
        #         if helper(indx + i):
        #             return True
        #     return False
        # return helper(0)
        # n = len(nums)
        # queue = deque([0])
        # visited = set([0])
        # while queue:
        #     curr_indx = queue.popleft()
        #     if curr_indx + 1 >= n:
        #         return True
        #     for nei_indx in range(1, nums[curr_indx] + 1):
        #         new_indx = curr_indx + nei_indx
        #         if new_indx >= n:
        #             return True
        #         if new_indx not in visited:
        #             queue.append(new_indx)
        #             visited.add(new_indx)
        # return False
        # at any point we will take the maximum
        n = len(nums)
        far = 0
        for i in range(len(nums)):
            if far < i:
                return False
            far = max(far , i + nums[i])
        return True


