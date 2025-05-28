import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        rows = min(n, k)
        queue = []
        for row in range(rows):
            heapq.heappush(queue, (matrix[row][0], row, 0))
        
        while k > 0:
            element, row, col = heapq.heappop(queue)
            if col < n - 1:
                heapq.heappush(queue, (matrix[row][col + 1], row, col + 1))
            k -= 1
        return element
