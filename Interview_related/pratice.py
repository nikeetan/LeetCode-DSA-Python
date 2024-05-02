#Insertion sort 
def selection_sort(arr):
    for i in range(len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
            #[4,5,3,2,1]
            #[3,4,5,2,1]
            #[2,3,4,5,1]
            #[1,2,3,4,5]
            print(arr)


    return arr

arr=[5,4,3,2,1]
print(selection_sort(arr))