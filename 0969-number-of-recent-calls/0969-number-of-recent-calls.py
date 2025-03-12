class RecentCounter:
    def __init__(self):
        self.counter=[]
        self.range=[]
    def binsearch(self,target,left,right):
        while left<right:
            mid=left+(right-left)//2
            if self.range[mid]==target:
                return mid
            elif self.range[mid]:
                left=mid+1
            else:
                right=mid-1
        return left
    def ping(self, t: int) -> int:
        if self.counter:
            self.range.insert(self.binsearch(t,0,len(self.range)-1),t)
            mini=t-3000
            maxi=t
            f_i=-1
            s_i=-1
            for i in range(len(self.range)):
                if mini<=self.range[i] and self.range[i]<=maxi:
                    if f_i==-1:
                        f_i=i
                    s_i=i
            self.counter.append(s_i-f_i+1)
        else:
            self.range.append(t)
            self.counter.append(1)
        return self.counter[-1]

            



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)