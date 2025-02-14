class ProductOfNumbers:
    def __init__(self):
        self.nums=[]
    def add(self, num: int) -> None:
        if len(self.nums)>=1:
            if self.nums[-1]==0:
                num*=1
            else:
                num*=self.nums[-1]
        self.nums.append(num)
    def getProduct(self, k: int) -> int:
        if len(self.nums)==k:
            if 0 in self.nums:
                return 0
            return self.nums[-1]
        else:
            if 0 in self.nums[-(k):]:
                return 0
            elif self.nums[-k-1]==0:
                return self.nums[-1]
            return self.nums[-1]//self.nums[-k-1]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)