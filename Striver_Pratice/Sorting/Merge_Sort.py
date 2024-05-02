def merge(array:list[int],low:int,mid:int,high:int):
    #left array index
    #0,mid
    #right array index
    #mid+1, high

    #Keep two pointers and then comparing and adding them into the list and once you complete any one of the list just merge the remaning as
    #because the list will be in a merged manner

    left=low
    right=mid+1
    print("left Sub array:",array[left:mid+1])
    print("Right Sub array:",array[right:high+1])
    temp=[]
    while ((left<=mid) and (right<=high)):
        if array[left]<array[right]:
            temp.append(array[left])
            left+=1
        else:
            temp.append(array[right])
            right+=1
    while left<=mid:
        temp.append(array[left])
        left+=1

    while right<=high:
        temp.append(array[right])
        right+=1

    # Now at this point we have left sorted array and right sorted array all put together in the original array

    print("Temp:",temp)
    print ("Array before temp making changes:",array)
    print("low:",low,"high:",high)
    for i in range(low,high+1):
        array[i]=temp[i-low]
    




def merge_sort_divide(array:list[int],low:int,high:int):
    mid=low+(high-low)//2
    if low==high:
        return 
    merge_sort_divide(array,low,mid)

    merge_sort_divide(array,mid+1,high)

    merge(array,low,mid,high)

    print("Array after temp making changes:",array)



array=[3,1,2,4,1,5,2,6,4]
low=0
high=len(array)-1
merge_sort_divide(array,low,high)
#print(array)
