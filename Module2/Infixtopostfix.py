def fetch_p(s:str):

    if s=='^':
        return 3
    elif s=='*' or s=='/':
        return 2
    elif s=='+' or s=="-":
        return 1
    else:
        return -1
    
def infix_to_postfix(stack:list[str],exp)->str:
    to_return=""
    for i in exp:
        
        if (i>='0' and i <'9') or (i>='a' and i<='z') or (i>='A' and i<='Z'):
            to_return+=i
        elif i=='(':
            stack.append(i)
        elif i==')':
            while stack[-1]!='(':
                to_return+=stack.pop()
            stack.pop()
        else:   
            while stack and (fetch_p(i)<=fetch_p(stack[-1])):
                to_return+=stack.pop()
            stack.append(i)
        print("Stack:", stack)
        print("Current character:", i)
        print("Current postfix:", to_return)
    while stack:
        to_return+=stack.pop()        
    return to_return


stack=[]
exp="A*(B+C)/D”"
print(infix_to_postfix(stack,exp))