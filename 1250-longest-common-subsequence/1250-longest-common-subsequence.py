'''
hash_map decrease the count whenever i get the commonm character

o(m)
o(n)

o(m) + o(n) + o(m)
o(m)

next thinking and maintain only one map so the movement i traverse the longer one in which i check the character map if that is greater than 1 occurance then i will decrease by 1 and increase the cnt if i have 0 then i will not do anything
whichever is smaller i will traverse that

'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]