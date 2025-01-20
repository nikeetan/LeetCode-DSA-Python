def binary_range(arr:list[int],target:int,low:int,high:int):
    # Left Growth
    range_l=[]
    while low<=high:        
        mid = low + (high-low)//2
        if arr[mid]==target:
            high=mid-1
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    if low<len(arr) and arr[low]==target:
        range_l.append(low)
    #Right Growth
    low,high=0,len(arr)-1
    while low<=high:
    
        mid = low + (high-low)//2
        if arr[mid]==target:
            low=mid+1
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    if high>=0 and arr[high]==target:
        range_l.append(high)
    return range_l




arr =[5,7,7,8,8,10]
target = 8
low = 0
high = len(arr) - 1
print(binary_range(arr,target,low,high))

