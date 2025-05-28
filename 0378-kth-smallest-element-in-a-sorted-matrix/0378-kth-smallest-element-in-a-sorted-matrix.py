import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def elemnt_cnt(mid, small, large):
            row = n - 1
            col = 0
            cnt = 0 
            while row >= 0 and col < n:
                if matrix[row][col] > mid:
                    large = min(large, matrix[row][col])
                    row -= 1
                else:
                    small = max(matrix[row][col], small)
                    cnt += row + 1 # full row elements
                    col += 1
            return cnt, small, large

       
        low = matrix[0][0]
        high = matrix[n - 1][n - 1]
        while low < high:
            mid = low + (high - low) // 2
            small, large = matrix[0][0], matrix[n - 1][n - 1]
            cnt, small, large = elemnt_cnt(mid, small, large)
            if cnt == k:
                return small
            elif cnt > k:
                high = small
            else:
                low = large
        return low

        '''
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
        '''

