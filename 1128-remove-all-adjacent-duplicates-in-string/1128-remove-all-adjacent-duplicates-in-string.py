# [a, y]
# 
#[a, y]
# a z x x z y
#.          p  
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) == 0:
            return s
        else:
            stk = []
            p = 0
            while p < len(s):
                if stk and stk[-1] == s[p]:
                    while stk and s[p] == stk[-1]:
                        stk.pop()
                else:
                    stk.append(s[p])
                p += 1
        return "".join(stk)
#TC : O(n)
#SC : O(n)