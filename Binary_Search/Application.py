class Binsearch:
    def linear_serach(self,array:list[int],element:int):
        first=-1
        last=-1
        for i in range(len(array)):
            if array[i]==element:
                if first==-1:
                    first=i
                    last=i
                else:
                    last=i
        return [first,last]
    def search(self,array:list[int],element:int,low:int,high:int):
        mid=(low)+(high-low)//2 # To avoid overflow
        prev=0
        if low>high:
            return -1
        else:
            if array[mid]==element:
                return mid
            elif array[mid]>element:
                return self.search(array,element,low,mid-1)
            elif array[mid]<element:
                return self.search(array,element,mid+1,high)
array=[1,2,3,3,3,3,3,3,3,3,4,5,6,7,8,10]
do=Binsearch()
element=3
print(do.linear_serach(array,element))

#print(do.search(array,element,low=0,high=len(array)-1))


