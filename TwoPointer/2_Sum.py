'''
Given a list and the target sum you need to have the two values adding to that can make up the target sum 

'''

class Twosum:
    def __init__(self,array,target):
        self.array=array
        self.target=target
        self.left=0
        self.right=len(self.array)-1

    def sum_operation(self):
        index_list=[]
        while self.left<self.right:
            sum=self.array[self.left]+self.array[self.right]
            if sum==self.target:
                index_list.append([self.left,self.right])
                return index_list
            elif sum>target:
                self.right-=1
            else:
                self.left+=1
        return False
    
array=[2,7,11,15]
target=9
compute=Twosum(array,target)
print(*compute.sum_operation())
                
        