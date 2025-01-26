class Solution:

    def __init__(self, w: List[int]):
        rs=w[0]
        for i in range(1,len(w)):
          rs+=w[i]
          w[i]=rs
        self.weights=w
        self.total_sum=rs

    def pickIndex(self) -> int:
        target= random.randint(1,self.total_sum)
        low,high=0,len(self.weights)
        while low<high:
          mid=low+(high-low)//2
          if self.weights[mid]<target:
            low=mid+1
          else:
            high=mid
        return low
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()