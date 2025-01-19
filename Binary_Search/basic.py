def search(element:int,array:list,high:int,low:int):
    if low>high:
        return -1
    else:
        mid=high-(high-low)//2
        print(mid,high,low,element,array[mid])
        if array[mid]==element:
            return "Element Found"
        elif array[mid]>element:
            return search(element,array,mid-1,low)
        elif array[mid]<element:
            return search(element,array,high,mid+1)
        else:
            return "Element Not Found"


    
    #let's say this as a linearapproch now using recurrsion

  
    # while low<=high:
    #     mid=high+(low-high)//2
    #     print(low,high,mid)
    #     if array[mid]==element:
    #         return 1
    #     if array[mid]<element:
    #         low=mid+1
    #     if array[mid]>element:
    #         high=mid-1
array=[1,2,3,4,5,6,7,8,9,10]
element=10
low=0
high=len(array)-1
#print(array[high])
print(search(element,array,high,low))


# def search(element, array, low, high):
#     if low > high:  # Base case for when the element is not found
#         return -1
    
#     mid = low + (high - low) // 2
    
#     if array[mid] == element:
#         return 1
#     elif array[mid] > element:
#         return search(element, array, low, mid-1)  # Corrected order and added return
#     else:
#         return search(element, array, mid+1, high)  # Added return

# # Example usage
# array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# element = 5
# result = search(element, array, 0, len(array) - 1)
# print(result)
# #print("Element found:", result == 1)
