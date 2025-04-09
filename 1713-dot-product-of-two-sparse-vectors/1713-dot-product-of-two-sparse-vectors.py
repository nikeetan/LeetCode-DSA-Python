class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec1 = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.vec1[i] = nums[i]
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        if (len(self.vec1) == 0) or (len(vec.vec1) == 0):
            return 0
        else:
            prod = 0
            
            if len(self.vec1) < len(vec.vec1):
                traverse = self.vec1
            else:
                traverse = vec.vec1
                vec.vec1 = self.vec1

            for i in traverse:
                if i in vec.vec1:
                    prod += traverse[i] * vec.vec1[i]
            return prod
            


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)