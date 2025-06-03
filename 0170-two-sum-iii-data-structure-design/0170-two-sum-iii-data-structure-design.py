class TwoSum:

    def __init__(self):
        self.nums = []
    def add(self, number: int) -> None:
        l , r = 0, len(self.nums) - 1
        while l <= r:
            mid = l + ( r - l) // 2
            if self.nums[mid] == number:
                l = mid + 1 
            elif self.nums[mid] < number:
                l = mid + 1
            else:
                r = mid - 1
        self.nums.insert(l, number)
        
    def find(self, value: int) -> bool:
       
        p1, p2 = 0, len(self.nums) - 1
        while p1 < p2:
            if self.nums[p1] + self.nums[p2] == value:
                return True
            elif self.nums[p1] + self.nums[p2] > value:
                p2 -= 1
            else:
                p1 += 1
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)