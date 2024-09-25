'''
maximum sub array sum
'''
class SlidingWindow:
    def __init__(self,array):
        self.array=array
        
    def compute(self,size):
        self.window_size=size
        curr=window_sum=sum(self.array[:self.window_size])
        for i in range(self.window_size,len(self.array)):
            curr-=self.array[i-self.window_size]
            curr+=self.array[i]
            window_sum=max(curr,window_sum)
        return window_sum
    def Compute_WWS(self):
        all_max=curr=self.array[0]
        p2=1
        while p2<len(self.array):
            curr=max(self.array[p2],curr+self.array[p2])
            all_max=max(curr,all_max)
            p2+=1
        return all_max
array=[3,1,2,3,4,5,6,7,8,9,9,9]
size=3
Maxi_Subarray=SlidingWindow(array)
print(Maxi_Subarray.compute(size))

array=[-2,1,-3,4,-1,2,1,-5,4]
Maxi_Subarray_WWS=SlidingWindow(array)
print(Maxi_Subarray_WWS.Compute_WWS())
        
        