class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def helper(openb,closeb):
            if ((openb==n) and (closeb==n)):
                res.append("".join(stack))
                return
            if openb<n:
                stack.append("(")
                helper(openb+1,closeb)
                stack.pop()
            if closeb<openb:
                stack.append(")")
                helper(openb,closeb+1)
                stack.pop()
        helper(0,0)
        return res