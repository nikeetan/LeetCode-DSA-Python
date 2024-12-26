def Permutation(array:list[int],stack:list[int],bl:list[int],n:int,marked:dict[int]):
    if n==len(array):
        bl.append(stack[:])
        return
    for i in range(len(array)):
        if marked[array[i]]!=1:
            marked[array[i]]=1
            stack.append(array[i])
            Permutation(array,stack,bl,n+1,marked)
            stack.pop()
            marked[array[i]]=0
array=[1,2,3]
n=0
stack=[]
bl=[]
marked={}
for i in range(len(array)):
    marked[array[i]]=0
Permutation(array,stack,bl,n,marked)
print(bl)