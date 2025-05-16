'''
again i can think of bfs herr
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque([(0, 0)])
        visited = set([0])
        n = len(nums)
        jumps = 0
        while queue:
            index, jumps = queue.popleft()
            if index >= n - 1:
                return jumps
            for step in range(1, nums[index] + 1):
                next_index = index + step
                if next_index < n and next_index not in visited:
                    visited.add(next_index)
                    queue.append((next_index, jumps + 1))
        
