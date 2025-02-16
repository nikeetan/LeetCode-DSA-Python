import heapq
class MedianFinder:

    def __init__(self):
        '''
        self.heap1=[]
        self.heap2=[]
        '''
        self.l1=[]
    
    def addNum(self, num: int) -> None:
        if len(self.l1)>0:
            l,r=0,len(self.l1)-1
            while l<=r:
                mid=l+(r-l)//2
                if num<self.l1[mid]:
                    r=mid-1
                else:
                    l=mid+1
            self.l1.insert(l,num)
        else:
            self.l1.insert(0,num)

        '''
        heappush(self.heap1,-num)
        heappush(self.heap2,-heappop(self.heap1))
        if len(self.heap2)>len(self.heap1):
            heappush(self.heap1,-heappop(self.heap2))
        '''
    def findMedian(self) -> float:
        if len(self.l1)%2==0:
            middle=len(self.l1)//2
            median=(self.l1[middle-1]+self.l1[middle])/2
        else:
            median=self.l1[(len(self.l1)//2)]
        return median        


        '''

        if len(self.heap1)>len(self.heap2):
            return -self.heap1[0]
        else:
            return (-self.heap1[0]+self.heap2[0])/2
        '''



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()