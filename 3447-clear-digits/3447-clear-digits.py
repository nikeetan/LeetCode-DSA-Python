class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if i>='0' and i<='9':
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack)