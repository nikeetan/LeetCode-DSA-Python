class ProductOfNumbers:
    def __init__(self):
        self.nums=[]
        self.index=-1
    def add(self, num: int) -> None:
        if num==0:
            self.index=len(self.nums)
            self.nums.append(1)
        else:
            if self.nums:
                num*=self.nums[-1]
            self.nums.append(num)
    def getProduct(self, k: int) -> int:
       
        if len(self.nums)==k:
            if self.index>=0:
                return 0
            return self.nums[-1]
        elif self.index<=len(self.nums)-k-1:
            return self.nums[-1]//self.nums[len(self.nums)-k-1]
        return 0
        
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)