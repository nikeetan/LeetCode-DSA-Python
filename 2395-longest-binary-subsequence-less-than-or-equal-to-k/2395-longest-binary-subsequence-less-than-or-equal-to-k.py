arr = [1, 2, 3]
arr = [[], [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]]
1001010
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        zeros = 0
        value = 0
        power = 1
        ones = 0
        for i in range(len(s)):
            if s[i] == '0':
                zeros += 1
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                power = power * 2
            elif s[i] == '1':
                if value + power <= k:
                    value = value + power
                    ones += 1
                power = power * 2 
                if power > k:
                    break
        return zeros + ones
                


        