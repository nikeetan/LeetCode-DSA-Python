'''
[4,5,6,7,0,1,2] target = 3
itr 1
l, r = 0, 6
mid = 3
if target == mid:
    return mid
elif target < mid and target >= lt:
    right = mid - 1
else:
    left = mid + 1
return - 1


itr 2
l, r = 4, 6
mid = 5

r = 4

itr 3
l,r = 4 + 4
mid = 4
4
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l)//2
            print(mid, l , r)
            if target == nums[mid]:
                return mid
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target > nums[mid] and target <= nums[r]:
                   l = mid + 1
                else:
                    r = mid - 1
        return -1
