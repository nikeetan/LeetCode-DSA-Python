'''
edge cases 

i am thinking of a backtrack approach where in my = current combination dosen't exceed 26
and the combination length is in bounds
every time i have two choices i can pick or not pick the next index if i pick then lets say
s = 1123
1 , 11 
1, 12, 
n * 2 **n

two lists one with individual and one with the combination
for every index i have 2 choices
(0), (0 , 1)
(1), (1, 2)
(2), (2, 3)
'''

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1 
        if s[n - 1] != '0':
            dp[n - 1] = 1
        else:
            dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            if s[i] != '0':
                dp[i] = dp[i + 1]
                if int(s[i : i + 2]) <= 26:
                    dp[i] += dp[i + 2]
            else:
                dp[i] = 0
        return dp[0]
        '''
        n = len(s)
        memo = {}
        ans = 0
        def helper(indx):
            if indx in memo:
                return memo[indx]
            if indx >= n:
                return 1
            if s[indx] == '0':
                return 0
            if indx == n - 1:
                return 1
            ans = helper(indx + 1)
            if int(s[indx : indx + 2]) <= 26:
                ans += helper(indx + 2)
            print("indx, ans", indx, ans)
            memo[indx] = ans
            return memo[indx]
        return helper(0)
        '''





            