'''
so the problem 

arr=[10,30,40,10,20,10,30]

take the sub array of size k and find the maximum of each sub_array

'''
class MaxSubarray:
    def __init__(self,array,window_size):
        self.array=array
        self.window_size=window_size
    def operation(self):
        start=0
        stop=1
        maxi=0
        maxi_list=[]
        while stop!=len(self.array)+1:
            if stop<self.window_size:
                stop+=1
            else:
                if maxi<max(self.array[start:stop]):
                    maxi=max(self.array[start:stop])
                maxi_list.append(maxi)
                start+=1
                stop+=1
                maxi=0
        return maxi_list
array=[0,9,10,3,1,15,-9,0,0,30,40]
#Expected o/p : [10,10,10,15,15,15,0,30,40] 
window_size=3
fetch=MaxSubarray(array,window_size)
print(fetch.operation())                
                



        