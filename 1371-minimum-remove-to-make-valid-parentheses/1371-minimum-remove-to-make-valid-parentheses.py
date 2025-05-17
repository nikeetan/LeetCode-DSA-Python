#TC : O(n)
#SC : O(n)

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        open_b = 0
        indx_to_remove = []
        for i, val in enumerate(s):
            if val == '(':
                open_b += 1
            elif val == ')':
                if open_b == 0:
                    s[i] = '*'
                else:
                    open_b -= 1
        if open_b > 0:
            for i in range(len(s)- 1, -1, -1):
                if open_b == 0:
                    break
                if s[i] == '(':
                    s[i] = '*'
                    open_b -= 1
        
        return "".join(c for c in s if c != '*')
                