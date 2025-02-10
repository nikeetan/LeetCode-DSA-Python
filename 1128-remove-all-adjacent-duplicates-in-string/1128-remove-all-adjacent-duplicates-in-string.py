class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        for i in s:
            if stack:
                if stack[-1]==i:
                    while stack and stack[-1]==i:
                        stack.pop()
                    continue
            stack.append(i)
        return ''.join(stack)
