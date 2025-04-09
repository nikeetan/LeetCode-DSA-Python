'''
Is the size of the two matrix same

There might be an empty nums1 while non empty num2 and also vice - versa

The output should be an input

we have to store sparse vector could you provide some more details on this part please

since i should store the sparse vector i am thinking something like a store by index as you said we have both nums1 and nums2 to be of same size we can formulate the store by index


if nums1 and (len(nums2) == 0):
    return 0
elif nums2 and (len(nums1) == 0):
    return 0

else:
// store this in the constructor
count = 0
globalself.vec 
{ 0 : [1, 0],
  1 : [0, 3],
  2 : [0, 0],
  3 : [2, 4],
  4 : [3, 0]
}



// Dot product obtained
res += numpy.prod(vector[indx])
return res
'''

class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec1 = {}
        for i in range(len(nums)):
            if i not in self.vec1 and nums[i] != 0:
                self.vec1[i] = nums[i]
        
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        for i in self.vec1:
            if i in vec.vec1:
                prod += self.vec1[i] * vec.vec1[i]
        return prod
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)