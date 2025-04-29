class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        mini = float('inf')
        for i in range(len(nums) - 2):
            for j in range(i + 1, len (nums) - 1):
                for k in range(j + 1,len(nums)):
                    if (nums[i] < nums[j]) and (nums[j] > nums[k]):
                        trip_sum = nums[i] + nums[j] + nums[k]
                        print(trip_sum)
                        if trip_sum < mini:
                            mini = trip_sum
        return mini if mini != float('inf') else - 1
                        
                         