'''
brute force approach would be 2 for loops o(n2)
second one would be the use of hash map
how? I would sort the array and then in that first occurance i would store and after that when i find the last occurance then i would subtract from the first and store it
'''

class Repeated:
    def __init__(self,array):
        self.array=array
    def operation(self):
        self.array=sorted(self.array)
        '''
        o(n)
        find till the last index
        '''
        first=0
        second=1
        d={}
        while second<len(self.array):
            if self.array[first]!=self.array[second]:
                d[self.array[first]]=abs(first-second)
                first=second
                second=second+1
            else:
                second=second+1
        to_subtract=0
        for key,value in d.items():
            to_subtract+=value
        if self.array[first] not in d:
            d[self.array[first]]=abs(len(self.array)-to_subtract)
        print(d)
        print(max(d,key=lambda x:d[x]))
   

        '''
        so this is a o(n) solution now maams lets think can i go with binary 
        '''


    
        
#array=[7,7,7,7,7,7,11,11,11,11,11,11,11,11,11,11,11,12,13]
array=[40,50,30,40,50,30,30,60,70,70]
fetch=Repeated(array)
fetch.operation()
            
        

        