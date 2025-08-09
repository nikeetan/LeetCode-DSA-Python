'''
[   9,  4,  7,  2,  10]

                   (10, 1)
'''


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        max_len = 0

        for j in range(n):
            for i in range(j):
                diff = nums[j] - nums[i]
                # If there's already a sequence ending at i with this diff, extend it
                if diff in dp[i]:
                    dp[j][diff] = dp[i][diff] + 1
                else:
                    dp[j][diff] = 2  # starting new sequence of length 2
                max_len = max(max_len, dp[j][diff])

        return max_len