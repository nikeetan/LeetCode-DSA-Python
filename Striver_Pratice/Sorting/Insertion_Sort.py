
from Bubble_Sort import swap

def Insertion_Sort(array:list[int]):
    for i in range(len(array)):
        j=i
        while j>0 and(array[j-1]>array[j]):
            array=swap(array,j,j-1)
            j-=1
    return array
array=[100,90,80,70,60,50,40,30]
print(Insertion_Sort(array))
        