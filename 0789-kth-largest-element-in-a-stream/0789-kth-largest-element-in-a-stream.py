import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)

    def find_pos(self,val):
        left , right = 0, len(self.nums) -1
        while left <= right:
            mid = left + (right - left )//2
            if self.nums[mid] == val:
                return mid
            elif self.nums[mid] < val:
                left = mid + 1 
            else:
                right = mid - 1
        return left
        

    def add(self, val: int) -> int:
        self.nums.insert(self.find_pos(val),val)
        return self.nums[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)