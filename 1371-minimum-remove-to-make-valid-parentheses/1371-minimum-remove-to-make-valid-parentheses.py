class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Garreeb approach
        p1=0
        stack=[]
        while p1<len(s):
            if s[p1]==')':
                if stack and stack[-1][0]=='(':
                    stack.pop()
                else:
                    stack.append([s[p1],p1])
            if s[p1]=='}':
                if stack and stack[-1][0]=='}':
                    stack.pop()
                else:
                    stack.append([s[p1],p1])
            if s[p1]==']':
                if stack and stack[-1][0]==']':
                    stack.pop()
                else:
                    stack.append([s[p1],p1])    
            if s[p1]=='(' or s[p1]=='{' or s[p1]=='[':
                stack.append([s[p1],p1])
            p1+=1
        indices=[]
        for i in stack:
            indices.append(i[-1])
        new_string=""
        for i in range(len(s)):
            if i not in indices:
                if new_string:
                    new_string+=s[i]
                else:
                    new_string=s[i]
            else:
                continue
        return new_string