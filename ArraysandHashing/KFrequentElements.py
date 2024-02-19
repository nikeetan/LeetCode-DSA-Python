from collections import defaultdict
import operator 
    
def topKFrequent(nums,k):
    d=defaultdict(int)
    for i in nums:
        d[i]+=1
    dummy=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
    l=[]
    count=0
    for key,value in dummy.items():
        if count==k:
            break
        else:
            l.append(key)
        count+=1
    return l
nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums,k))

