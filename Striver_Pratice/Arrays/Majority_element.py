'''
Boyer -More Algorithm

Take two pointers one would store the element and another 
would keep track of the occurance as soon as the element reaches 0 assign 
the new element to the variable in which you have store the element earlier.

'''
class BM_Algo:
    def __init__(self,array):
        self.array=array
    def operation(self):
        ele_store=0
        count_store=0
        for i in self.array:
            if count_store==0:
                ele_store=i
            if i==ele_store:
                count_store+=1
            else:
                count_store-=1
        return ele_store

#I/P:
array=[1,2,2,2,2,4,5,6,2]
Majority_ele=BM_Algo(array)
print(Majority_ele.operation())

# Traversal:
'''
ele_store =1
count_store=1

ele_store =1 
count_store=0

ele_store =2 
count_store=1

ele_store =2 
count_store=2

ele_store =2 
count_store=3

ele_store =2 
count_store=4

ele_store =2 
count_store=3

ele_store =2 
count_store=2

ele_store =2 
count_store=1

ele_store =2 
count_store=0
'''








        
