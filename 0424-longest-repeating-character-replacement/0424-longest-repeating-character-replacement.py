'''
A A B C D E G
max = 2
when we slide
max will still be 2
'''

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxf = 0
        count = defaultdict(int)
        res = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            


