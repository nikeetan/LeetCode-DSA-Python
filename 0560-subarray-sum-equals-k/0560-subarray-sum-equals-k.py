'''
1 intra - 2 tagdre 3 barteti ?

[1, -1, 0] K = 0
running_sum = 1
is 1 == k no is 1 - 3 = -2 in k
num_map = { 1  :  1, 2 : 1, 3 : 1}

'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_map = {0 : 1}
        cnt = 0
        running_sum = 0
        for i in nums:
            running_sum += i
            if running_sum - k in num_map:
                cnt += num_map[running_sum - k]
            if running_sum not in num_map:
                num_map[running_sum] = 1
            else:
                num_map[running_sum] += 1
        return cnt

            
