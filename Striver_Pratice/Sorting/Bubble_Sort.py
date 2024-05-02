def swap(array:list[int],min:int,max:int):
    array[max],array[min]=array[min],array[max]
    return array 
def Bubble_Sort(array:list[int]):
    for i in range(0,len(array)):
        for j in range(0,len(array)-1-i):
            if array[j]>array[j+1]:
                array=swap(array,j+1,j)
    return array
if __name__ == '__main__':
    array=[1,60,50,40,30,20,10]
    print(Bubble_Sort(array))