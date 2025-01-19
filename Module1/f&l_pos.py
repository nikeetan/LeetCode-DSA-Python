def binary_range(arr:list[int],target:int,low:int,high:int):
    # Left Growth
    range_l=[]
    while low<high:
        mid = low + (high-low)//2
        if arr[mid]==target:
            high=mid
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    range_l.append(high)
    #Right Growth
    low,high=0,len(arr)-1
    while low<high:
        mid = low + (high-low)//2
        if arr[mid]==target:
            low=mid
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    range_l.append(low)
    return range_l




arr=[3,9,9,9,11,12]
low,high=0,len(arr)-1
target=9
print(binary_range(arr,target,low,high))

