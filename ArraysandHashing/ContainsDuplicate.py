class Solution:

    def containsDuplicate(nums):
        if len(set(nums))==len(nums):
            return False
        return True

nums = [1,2,3,45,1]
a=Solution
print(a.containsDuplicate(nums))
