class hash:
    def __init__(self,array:list):
        self.array=array
        
    def operation(self):
        d={}
        for i in self.array:
            
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        return d

array=[10,20,30,40,50,60,10,20,30]
hashing=hash(array)
k=hashing.operation()
print(k)        

