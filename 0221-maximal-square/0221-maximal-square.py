# class Solution:
#     def maximalSquare(self, matrix: List[List[str]]) -> int:
#         '''
#         memoization 
#         '''
#         R = len(matrix)
#         C = len(matrix[0])
#         dp = [[0 for i in range(C)] for j in range(R)]
#         max_ans = float('-inf')
#         '''
#         fill out 1st row and col 
#         '''
#         for i in range(C):
#             if matrix[0][i] == '1':
#                 dp[0][i] = 1
#             else:
#                 dp[0][i] = 0
#             max_ans = max(max_ans, dp[0][i])

#         for i in range(R):
#             if matrix[i][0] == '1':
#                 dp[i][0] = 1
#             else:
#                 dp[i][0] = 0
#             max_ans = max(max_ans, dp[i][0])
        
#         for i in range(1, R):
#             for j in range(1, C):
#                 if matrix[i][j] == '1':
#                     dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i- 1][j]) + 1
#                 else:
#                     dp[i][j] = 0
#                 max_ans = max(max_ans, dp[i][j])
#         return max_ans * max_ans
class Solution:
    def maximalSquare(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        dp = [0] * (cols + 1)
        maxsqlen = 0
        prev = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(dp[j - 1], prev, dp[j]) + 1
                    maxsqlen = max(maxsqlen, dp[j])
                else:
                    dp[j] = 0
                prev = temp
        return maxsqlen * maxsqlen