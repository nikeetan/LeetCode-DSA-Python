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

    def rfgrowth(self,array:list[int],element:int,low:int,high:int):
        # Left order growth
        l=[]
        while low<=high:
            mid = low+(high-low)//2
            if array[mid]==element:
                high=mid-1
            elif array[mid]<element:
                low=mid+1
            else:
                high=mid-1
        l.append((low))
        low = 0
        high = len(array)-1
        while low<=high:
            mid = low+(high-low)//2
            if array[mid]==element:
                low=mid+1
            elif array[mid]<element:
                low=mid+1
            else:
                high=mid-1
        l.append((high))
        return l



    
array=[1,2,3,3,3,3,3,3,3,3,4,5,6,7,8,10]
do=Binsearch()
element=3
print(do.rfgrowth(array,element,low=0,high=len(array)-1))



