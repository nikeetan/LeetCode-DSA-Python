def swap(array,i,j):
    array[i],array[j]=array[j],array[i]
    return array

def Selection_Sort(array:list[int]):
    for i in range(len(array)-1):
        mini=i 
        for j in range(i+1,len(array)):
            if array[mini]>array[j]:
                mini=j
        array=swap(array,i,mini)
    return array

array=[30,40,20,10,70,2,3,1]
print(Selection_Sort(array))