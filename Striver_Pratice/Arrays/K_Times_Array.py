class Times_Array:
    def __init__(self,array,k):
      self.array=array
      self.k=k
    def operation(self):
       count=0
       indx=0
       while True:
        indx=(indx+1)%len(self.array)
        if indx==1:
            count+=1
            if count==self.k+1:
                break
            print("Printing for the {}th time".format(count))
        print(self.array[indx])
        indx+=1


array=[1,2,3,4,5,6,7]
k=3
fetch=Times_Array(array=array,k=k)
fetch.operation()
             
    
        