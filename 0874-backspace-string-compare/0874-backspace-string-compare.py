class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def funcheck(st):
            stack=[]
            for i in st:
                if i=='#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(i)
            return stack
        return funcheck(s)==funcheck(t)