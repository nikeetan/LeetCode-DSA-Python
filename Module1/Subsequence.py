def permutation(sl:list[int],bl:list[int],n:int,array:list[int],pointer:int):
    if pointer==n:
        bl.append(sl)
        return
    permutation(sl+[array[pointer]],bl,n,array,pointer+1)
    permutation(sl,bl,n,array,pointer+1)

array=[1,2,3]
n=len(array)
bl=[]
sl=[]
pointer=0
permutation(sl,bl,n,array,pointer)
print(bl)