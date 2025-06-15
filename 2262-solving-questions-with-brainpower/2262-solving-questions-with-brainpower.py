class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, - 1, -1):
            points = questions[i][0]
            skip = questions[i][-1]
            next_indx = i + skip + 1
            if next_indx < n:
                dp[i] = max(dp[i + 1], points + dp[next_indx])
            else:
                dp[i] = max(dp[i + 1], points)
        return dp[0]