def subsequence(sl,bl,index,length,number):
    if index==length:
        bl.append(sl[:])
        return
    
    subsequence(sl+[number[index]],bl,index+1,length,number)
    subsequence(sl,bl,index+1,length,number)
number=[1,2,3]
sl,bl=[],[]
index,length=0,len(number)
subsequence(sl,bl,index,length,number)
print(bl)