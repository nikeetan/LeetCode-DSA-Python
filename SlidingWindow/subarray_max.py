from collections import deque 
class sliding_max:
    def __init__(self,array,size,window_size):
        self.array=array
        self.size=size
        self.ws=window_size

    def sub_max_op(self):
        max_subarray=deque()
        for i in range(self.size):
            # operations
            #1 push back the index to the deque verifying this is in increasion order
            #2 pop from the front of my  curreny index - window size gives me the 0th element
            #3 while pushing ensure the deque is in decreasing order if it's not pop till the deque turns out to be decreasing
            #4 the front element of the deque is the maximum now after completing the window size please do append the item to the list.
            max_subarray.append(i)
        print(max_subarray)








array=[10,20,30,40,50,60,70,80,90,100]
window_size=3
SubArray_max=sliding_max(array,len(array),window_size)
SubArray_max.sub_max_op()


        