from collections import Counter
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # Longest subsequence atleast k times so we need to take the characters which are atleast k times repeated
        ktimesChar = []
        for key, val in Counter(s).items():
            if val >= k:
                ktimesChar.append(key)
        ktimesChar = sorted(ktimesChar, reverse = True)
        q = deque(ktimesChar)
        ans = ""
        nxt_char = ""
        while q:
            curr_char = q.popleft()
            if len(curr_char) > len(ans):
                ans = curr_char
            for ch in ktimesChar:
                nxt_char = curr_char + ch
                it = iter(s) # ordered checking    
                if all(ch in it for ch in nxt_char * k):
                    q.append(nxt_char)
        return ans

