class Reverse:
    def __init__(self,array):
        self.array=array
    def Operation(self,new_list,size):
        if size<0:
            return new_list
        else:
            new_list[(len(new_list)-1)-size]=self.array[size]
            self.Operation(new_list,size-1)

array=[1,2,3,4,5]
R=Reverse(array)
new_list=[0]*len(array)
R.Operation(new_list,len(array)-1)
print(new_list)
