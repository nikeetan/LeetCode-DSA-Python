class swap:
    def __init__(self,array,great_index,small_index):
        self.Array=array
        self.Great_index=great_index
        self.Small_index=small_index
    def swap_operation(self):
        temp=self.Array[self.Great_index]
        self.Array[self.Great_index]=self.Array[self.Small_index]
        self.Array[self.Small_index]=temp
        return self.Array

class sort:
    def __init__(self,array,size):
        self.Array=array
        self.Size=size
    
    def bubble_sort(self):
        for i in range(0,((self.Size-2)+1)):
            for j in range(0,((self.Size-2-i)+1)):
                if self.Array[j+1]<self.Array[j]:
                    swap_object=swap(self.Array,j,j+1)
                    self.Array=swap_object.swap_operation()
        return self.Array

array=[10,20,1,2,3,4,5,6,3,4,5,10,20,4,1,0]
size=len(array)    

sorted_array=sort(array,size)
#print(sorted_array.bubble_sort())
