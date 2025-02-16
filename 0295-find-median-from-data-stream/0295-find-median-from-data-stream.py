class MedianFinder:

    def __init__(self):
        self.list1=[]
    
    def addNum(self, num: int) -> None:
        self.list1.append(num)

    def findMedian(self) -> float:
        self.list1=sorted(self.list1)
        if len(self.list1)%2==0:
            middle=len(self.list1)//2
            median=(self.list1[middle-1]+self.list1[middle])/2
        else:
            median=self.list1[(len(self.list1)//2)]
        return median        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()