'''
Here we fetch the number of unique elements in the list after the removal of k elements from the list.
'''
import collections


class Fetch_least:
    def __init__(self,array,k):
        self.array=array
        self.k=k
        self.count=0

    def operation(self):
        occurance_dictionary=collections.Counter(self.array)
        occurance_list=list(occurance_dictionary.values())
        occurance_list.sort()
        for i in range(len(occurance_list)):
            if self.k>=occurance_list[i]:
                self.k-=occurance_list[i]
                occurance_list[i]=0
            else:
                occurance_list[i]-=self.k
                self.k=0
            if occurance_list[i]==0:
                self.count+=1

        return self.count
    
array=[4,3,1,1,3,3,2]
k=3
Unique_elements=Fetch_least(array,k)
print(Unique_elements.operation())
