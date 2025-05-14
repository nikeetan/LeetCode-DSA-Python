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
        # TC :  O(m x n)
        # SC :  O(m x n)

        
        dp = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        max_ans = float('-inf')
        # copy first row corresponding elements 

        # for i in range(len(matrix)):
        #     if matrix[i][0] == '1':
        #         dp[i][0] = 1
        #     else:
        #         dp[i][0] = 0
        #     max_ans = max(max_ans, dp[i][0])

        # # copy first col
        # for i in range(len(matrix[0])):
        #     if matrix[0][i] == '1':
        #         dp[0][i] = 1
        #     else:
        #         dp[0][i] = 0
        #     max_ans = max(max_ans, dp[0][i])
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0 or j == 0:
                    if matrix[i][j] == "1":
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                elif matrix[i][j] == "1":
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j], dp[i][j-1]) + 1
                else:
                    dp[i][j] = 0
                max_ans = max(max_ans, dp[i][j])
        return max_ans * max_ans


        
