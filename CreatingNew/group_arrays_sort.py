class Group_sort:
    def __init__(self,array1,array2):
        self.array1=array1
        self.array2=array2
    def operation(self):
        length=len(self.array1)
        new_array=[(self.array1[i],self.array2[i]) for i in range(length)]
        new_array=sorted(new_array)
        return new_array
def __main__():
    capital=[3,2,0]
    profit=[2,1,100]
    k=Group_sort(capital,profit)
    print(k.operation())

__main__()
        