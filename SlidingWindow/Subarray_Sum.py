class Subarray:
    def __init__(self,array,subarray_size):
        self.array=array
    def max_sub_array(self):
        #Approach 1 o(n^2)
        size=len(self.array)
        sum_subarray=[]
        i,j,sum=0,0,0
        while j<size:
            if j-i+1<subarray_size:
                print(j)
                #print(self.array[j])
                sum+=self.array[j]
                j+=1
            else:
                sum+=self.array[j]
                sum_subarray.append(sum)
                sum-=self.array[i]
                j+=1
                i+=1
        print(sum_subarray)
         
        #o(n2)

        # for i in range(size-subarray_size+1):  
        #     sum=0
        #     for j in range(i,i+subarray_size):
        #         sum+=self.array[j]
        #     sum_subarray.append(sum)
        # print(sum_subarray)

        #o(n)
                

        # for i in range(size-subarray_size+1):
        #     for j in range(i,i+subarray_size):
        #         print(self.array[j])


array=[10,20,30,40,50,60,70,80,90,100]
subarray_size=3
subarraysum=Subarray(array,subarray_size)
subarraysum.max_sub_array()