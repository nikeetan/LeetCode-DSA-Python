def Subsequence(sl:list[int],bl:list[int],n:int,array:list[int],pointer:int):
    if pointer==n:
        bl.append(sl)
        return
    Subsequence(sl+[array[pointer]],bl,n,array,pointer+1)
    Subsequence(sl,bl,n,array,pointer+1)

array=[1,2,3]
n=len(array)
bl=[]
sl=[]
pointer=0
Subsequence(sl,bl,n,array,pointer)
print(bl)