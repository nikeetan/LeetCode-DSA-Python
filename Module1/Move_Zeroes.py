arr=[0, 1, 0, 3, 12, 0, 0, 4, 0, 5, 0, 0, 6, 0, 7, 8, 0, 9, 0, 0]
p1=0
p2=1
while p2<len(arr):
    if arr[p1]!=0:
        p1+=1
    if arr[p1]==0 and arr[p2]!=0:
        arr[p1],arr[p2]=arr[p2],arr[p1]
        p1+=1
    p2+=1
print(arr)
