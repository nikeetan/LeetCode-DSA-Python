class Builtin:
    def __init__(self,array1,array2):
        self.array1=array1
        self.array2=array2
    def operation(self):
        for a,b in zip(self.array1,self.array2):
            print(a,b)
        '''
        club_sort=[(self.array1[i],self.array2[i]) for i in range(n)]
                '''
array1=[2,3,4,5,6]
array2=[7,8,9,10,11]
fetch=Builtin(array1,array2)
print(fetch.operation())



        