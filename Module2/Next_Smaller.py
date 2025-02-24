l=[4,8,5,2,25]
stack=[]
p2=len(l)-1
to_return=[0]*len(l)
count=len(stack)-1
while p2>=0:
    if stack:
        while stack and l[stack[-1]]>l[p2]:
            stack.pop()
        if not (stack):
            stack.append(-1)
    else:
        stack.append(-1)
    if stack[-1]!=-1:
        to_return[count]=l[stack[-1]]
    else:
        to_return[count]=-1
    count-=1
    stack.append(p2)
    p2-=1

print(to_return)
