'''

so the idea is using sliding window in that let me first create the size of the window once I encounter the window just raise the flag 

Now after the flag is raised i just need to push one element and pop one element in the list 

After that i need to traverse the sub array and then add the values to the dictionary i mean the ocuurance see what i think is every time

i will create the dictionary newly because searching the element which is not in the sub array and then deleting it probably takes O(n)

'''


class Unique:
    def __init__(self,array,window):
        self.array=array 
        self.window=window
    def create_dictionary(self,subarray):
        '''
        send the sub array everytime and traverse the array and find the elements and push it into the dictionary
        '''
        new_dict={}
        count=0
        for i in subarray:
            if i not in new_dict:
                new_dict[i]=1
                count+=1
            else:
                new_dict[i]+=1
        return count
        
            

    def fetch_subarray(self):
        '''
        here first create a flag variable set it up to 0 till the window size is not met
        once the window size is met fetch the sub array and send it to create dictionary

        exit condition should be stop pointer being at the end of the list
        and then return subarray
    
        '''
        flag=0
        start=0
        stop=1
        Unique_subarray=[]
        while stop!=len(self.array)+1:
            if stop==self.window:
                flag=1
            if flag==1:
                sub_array=self.array[start:stop]
                unique_count=self.create_dictionary(sub_array)
                Unique_subarray.append(unique_count)
                start+=1
                stop+=1
            else:
                stop+=1
            
        return Unique_subarray

array=[0]
window=4
fetch=Unique(array,window)
print(fetch.fetch_subarray())
