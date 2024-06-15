import heapq
from group_arrays_sort import Group_sort

def fun(rng1,new_array):
    k=2
    rng=rng1
    j=0
    w=0
    maxHeap=[]
    print("New_array:", new_array)
    for i in range(k):
        while j<rng and new_array[j][0]<=w:
            heapq.heappush(maxHeap,-new_array[j][1])
            j+=1
        if not maxHeap:
            break
        print("heap Before pop:",maxHeap)
        w-=heapq.heappop(maxHeap)
        print("heap after pop:",maxHeap)

    return w            




capital=[0,1,1]
profit=[1,2,3]
group=Group_sort(capital,profit)
new_array=group.operation()
rng1=len(profit)
print(fun(rng1,new_array))







