def permutations(number,sl,bl,index,length):
    total=0 
    if index==length:
        total+=1
    for i in range(length):
        if number[i] not in marked:
            marked[number[i]]=1
            total+=permutations(number,sl+[number[i]],bl,index+1,length)
            del marked[number[i]]
    return total
number=[1,2,3]
sl,bl,marked=[],[],{}
index,length=0,len(number)
print(permutations(number,sl,bl,index,length))

