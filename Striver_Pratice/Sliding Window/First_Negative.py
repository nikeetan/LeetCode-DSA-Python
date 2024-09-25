def printFirstNegativeInteger( A, N, K):
    # code here
    '''
    i will take a list and push only negative number in that just like stack so that 
    the first element would be always negative but how would i pop it based on window
    i think this works let me try 
    '''
    Negative_list=[]
    to_return=[]
    for i in range(K):
        if A[i]<0:
            Negative_list.append(A[i])
    for i in range(K,len(A)):
        if A[i-K]<0 and Negative_list[0]==A[i-K]:
            ele=Negative_list.pop(0)
            to_return.append(ele)
        elif len(Negative_list)==0:
            to_return.append(0)
        else:
            to_return.append(Negative_list[0])
        if A[i]<0:
            Negative_list.append(A[i])
        else:
            continue
    return to_return

N=5
A=[-8,2,3,-6,10]
K=2
print(printFirstNegativeInteger(A,N,K))
