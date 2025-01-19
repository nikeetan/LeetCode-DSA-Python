def binary_search(arr:list[int],target:int,low:int,high:int):
    if low<=high:
        mid=low+(high-low)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            return binary_search(arr,target,low=0,high=mid-1)
        else:
            return binary_search(arr,target,low=mid+1,high=high)
    else:
        return -1

arr=[1,2,3,4,5,6,7,8,9,10]
target=100
low=0
high=len(arr)-1
print(binary_search(arr,target,low,high))