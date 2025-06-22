'''
convert word1 to word2
lets say word1 is empty then i will have to insert all the characters
or else word2 is empty and i a
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        # both are empty
        for row in range(len(dp) -1, -1, -1):
            for col in range(len(dp[0]) -1, -1, -1):
                # Base case when both are empty that is word1 = "" word2 = ""
                #print(row, col)
                if row >= len(word1) and col >= len(word2):
                    dp[row][col] = 0
                # if either among one is empty lets say word1 is empty and word2 is non empty no of operations = len(word2) right
                elif row >= len(word1):
                    dp[row][col] = len(word2) - col
                elif col >= len(word2):
                    dp[row][col] = len(word1) - row
                else:
                    #print(row, col)
                    if word1[row] == word2[col]:
                        dp[row][col] = dp[row + 1][col + 1]
                    else:
                        dp[row][col] = 1 + min(dp[row][col + 1],dp[row + 1][col],dp[row + 1][col + 1])
        return dp[0][0]
            
        