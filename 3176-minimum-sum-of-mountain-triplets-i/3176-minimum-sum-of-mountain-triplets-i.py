class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return - 1
    
        mini, maxi = nums[0], nums[-1]
        min_list, max_list  = [nums[0]], [nums[-1]]

        for i in range(1, len(nums)):
            if nums[i] < mini:
                mini = nums[i]
            min_list.append(mini)
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < maxi:
                maxi = nums[i]
            max_list.insert(0, maxi)

        mini_sum = float('inf')

        for i in range(1, len(nums) - 1):
            if min_list[i-1] < nums[i] > max_list[i + 1]:
                mini_sum = min(mini_sum , (min_list[i-1]  + nums[i] + max_list[i + 1] ))

        return -1 if mini_sum == float('inf') else mini_sum

    