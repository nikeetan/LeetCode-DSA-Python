class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix_sum = len(self.nums)*[0]
        prefix_sum[0]=self.nums[0]
        for i in range(1,len(self.nums)):
            prefix_sum[i]=self.nums[i]+prefix_sum[i-1]
        if left-1 < 0:
            return prefix_sum[right]
        else:
            return prefix_sum[right]-prefix_sum[left-1]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)