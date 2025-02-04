class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=='(' or i=='[' or i=='{':
                stack.append(i)
            else:
                if stack:
                    if i==')' and stack[-1]!='(':
                        return False
                    if i==']' and stack[-1]!='[':
                        return False
                    if i=='}' and stack[-1]!='{':
                        return False
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        else:
            return True