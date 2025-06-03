'''
fix one pointer at the 0th location 
and start the second pointer at the 0th location
when i reach the length of dictionary > 2 i will compute the window size

then i will move the first pointer

'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        ans = float('-inf')
        for i in range(len(s)):
            d = {}
            for j in range(i, len(s)):
                d[s[j]] = 1
                if len(d) > 2:
                    break
                ans = max(ans, j - i + 1)
        return ans
        