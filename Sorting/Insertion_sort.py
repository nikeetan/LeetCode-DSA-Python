from Bubble_sort import swap
class Insertion_sort:
    def __init__(self,array,size):
        self.Array=array
        self.size=size
    def sort_operation(self):
        for i in range(1,self.size):
            key=self.Array[i]
            j=i-1
            while j>=0 and self.Array[j]>key:
                self.Array[j+1]=self.Array[j]
                j=j-1
            self.Array[j+1]=key
        return self.Array
        
array=[10,20,30,4,1,2,3]
size=len(array)
insertion_sort=Insertion_sort(array,size)
print(insertion_sort.sort_operation())
