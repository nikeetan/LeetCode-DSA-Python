class sequential_search:
    def __init__(self,array,size,key):
        self.Array=array
        self.Size=size
        self.key=key
    def search_operation(self):
        for i in range(self.Size):
            if self.key==self.Array[i]:
                return "Element found at index:",i
        return "Element is not found"
    
Array=[1,2,3,4,5,6,7,9,20]
size=len(Array)
key=20

sequence_search=sequential_search(Array,size,key)
print(sequence_search.search_operation())
