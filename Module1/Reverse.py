arr=[1,2,3,4,5,6,7,8,9,10]
p1=0
p2=len(arr)-1
while p1<p2:
    arr[p1],arr[p2]=arr[p2],arr[p1]
    p1+=1
    p2-=1
print("The Reveresed Array is:",arr)


