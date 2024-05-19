'''
Inorder to find the GCD of two numbers we should find the list of common factors and in that which one seems to be the greatest 

should return that so for that sum this step is the part of the program

'''
class Intersect:
    def __init__(self,l1:list,l2:list):
        self.list1=l1
        self.list2=l2
    operation=lambda self: [x for x in self.list1 if x in self.list2]


list1=list(map(int,input("Enter the list1: ").split()))
list2=list(map(int,input("Enter the list2: ").split()))
common=Intersect(list1,list2)
print(common.operation())