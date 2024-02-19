class Binarysearch:
    #Always works for sorted array

    def __init__(self,Array,left,right,key):
        self.Array=Array
        self.left=left
        self.right=right
        self.key=key
    def search_operation(self):
        while self.left<=self.right:
            mid=self.left+(self.right-self.left)//2
            if self.Array[mid]==self.key:
                return "The element is found at index:{}".format(mid+1)
            if self.key<self.Array[mid]:
                self.right=mid-1
            if self.key>self.Array[mid]:
                self.left=mid+1
        return "The element {} is not found in the array".format(self.key)

Array=[1,2,3,4,5,6,7,8,9,10]
left=0
right=len(Array)-1
key=1
search=Binarysearch(Array,left,right,key)
print(search.search_operation())
