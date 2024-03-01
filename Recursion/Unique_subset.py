'Unique subset of the given array '
'1. Fetch the subsets that are not repeating'
'arr={1,2,2}'
'Here the subsets will be {{},{1},{2},{1,2},{2,2},{1,2,2}}'
'Approach we will follow the same subset sum appproach only but in here i will have to take set so as to not include the repetative subsets'

def function(indx:int,arr:list,n:int,subset:set,k1:list):
    if n==indx:
        k1=tuple(k1)
        subset.add(k1)
    else:
        k1.append(arr[indx])
        function(indx+1,arr,n,subset,k1)
        k1.pop()
        function(indx+1,arr,n,subset,k1)

arr=[1,2,2]
n=3
subset=set()
k1=[]
indx=0
function(indx,arr,n,subset,k1)
print(subset)
