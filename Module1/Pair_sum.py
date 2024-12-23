arr=[2,3,5,7,11,13]
p1=0
p2=len(arr)-1
target=14
to_return=[]
while p1<p2:
    if arr[p2]+arr[p1]==target:
        to_return.append((arr[p1],arr[p2]))
        break
    elif arr[p1]+arr[p2]>target:
        p2-=1
    else:
        p1+=1
print("The elements which add upto the following sum are:",to_return)