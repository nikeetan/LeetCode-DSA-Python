'''
" a     b   a   b"
                    p1
                    p2
[a, ab, aba, abab, b, ba, bab]
'''

class Solution:
    def lastSubstring(self, s: str) -> str:
        p1, p2 = 0 , 1
        k =  0
        while p2 + k < len(s):
            if s[p1 + k] == s[p2 + k]:
                k += 1
                continue
            elif s[p1 + k] > s[p2 + k]:
                p2 = p2 + k + 1
            else:
                p1 = max(p1 + k + 1, p2)
                p2 = p1 + 1
            k = 0
        return s[p1: ]