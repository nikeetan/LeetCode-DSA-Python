# Solution using Hashmap
from collections import defaultdict
class solution:
    def TwoSum(self, nums,target):
        d=defaultdict(int)
        for i,n in enumerate(nums):
            difference=target-n
            if difference in d:
                return [d[difference],i]
            else:
                d[n]=i
        return ""


nums=[1,9,6,3,5,4,2,100]
target=101
a=solution()
print(a.TwoSum(nums,target))

