import numpy as np
def ProductOfArray(nums):    
    x=np.array(nums)
    if 0 in nums:
        k1=nums.index(0)
        k=np.where(x!=0,np.product(x)//x,np.product(np.delete(x,k1)))
    else:
        k=np.product(x)//x
    return list(k)


nums=[-1,1,0,-3,3]
print(ProductOfArray(nums))
