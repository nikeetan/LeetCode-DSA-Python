class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0
        queue = deque()
        res = []
        while r < len(nums):
            while queue and queue[-1][-1] < nums[r]:
                queue.pop()
            queue.append((r, nums[r]))
            if r - l + 1 == k:
                res.append(queue[0][1])
                if l == queue[0][0]:
                    queue.popleft()
                l += 1
            r += 1
        return res
