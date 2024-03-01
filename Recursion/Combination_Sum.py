def Combined_Target(indx:int,size:int,target:int,array:list,combinations:set,dummy:list):
    if indx==size:
        if target==0:
            combinations.add(tuple(dummy))
        return 
    if array[indx]<=target:
        dummy.append(array[indx])
        Combined_Target(indx,size,target-array[indx],array,combinations,dummy)
        dummy.pop()
    Combined_Target(indx+1,size,target,array,combinations,dummy)

array = [2,3,6,7]
target = 7
size=len(array)
indx=0
combinations=set()
dummy=[]

Combined_Target(indx,size,target,array,combinations,dummy)
k=[]
for i in combinations:
    k.append(list(i))
print(k)
