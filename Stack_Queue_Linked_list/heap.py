'''
Implemented on the basis of priority queue

Prority queue is the one in which the element with the highest priority is taken out first
lets say we have the elements with the priority

T1-5

T2-6

T3-8

T4-2

T5-1

Now the queue will be interested to return the element T1 as it as the highest priority


so heap is a Tree Data Structure in this there are two variations that is min heap and max heap so in min heap we will be having 
all the parent nodes

also the insertion here is logarithmic complexity and hence it is faster.

Now in min heap the parent nodes are always said to be smaller than the child nodes that is:
                                   p= 4
                               c1= 20   c2=30

first child is at the index 2*i+1 and second child is at the index 2*i+2 

Now in the max heap the case is said to be different the parent node is always having the largest value than the child nodes
                                    p=20
                                c1=4    c2=5    

'''


import heapq

data=[100,20,30,40,1,2,3,45,6,7]
heapq.heapify(data)
heapq.heappush(data,0)
heapq.heappushpop(data,-2)
z=heapq.heappop(data)
heapq._heapify_max(data)
#print(z)
print(data)
