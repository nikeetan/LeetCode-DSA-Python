class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if self.arr:
            left , right = 0, len(self.arr) - 1 
            while left <= right:
                mid = left + (right - left) //2
                if self.arr[mid] == num:
                    self.arr.insert(mid, num)
                    return
                elif self.arr[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            self.arr.insert(left, num)
        else:
            self.arr.insert(0, num)

    def findMedian(self) -> float:
        if len(self.arr)%2 == 0:
            mid = (len(self.arr) + 1) //2
            return (self.arr[mid - 1] + self.arr[mid])/2
        else:
            return self.arr[len(self.arr) // 2] 
    
         


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()