class swap:
    def __init__(self,Array,greater_index,small_index):
        self.Array=Array
        self.greater_index=greater_index
        self.small_index=small_index

    def swap_operation(self):
        temp=self.Array[self.greater_index]
        self.Array[self.greater_index]=self.Array[self.small_index]
        self.Array[self.small_index]=temp

        return self.Array

class SelectionSort:
    def __init__(self,Array,size):
        self.Array=Array
        self.size=size
    def SelectionSort(self):
        for i in range(0,(self.size-1)):
            minimum=i
            for j in range(i+1,(self.size)):
                if self.Array[j]<self.Array[minimum]:
                    minimum=j
            swapp_object=swap(self.Array,i,minimum)
            self.Array=swapp_object.swap_operation()
        return self.Array

Array=[10,20,30,40,50,1,2,3,4,5]
selection=SelectionSort(Array,len(Array))
Select_sort=selection.SelectionSort()
#print(swapped)

