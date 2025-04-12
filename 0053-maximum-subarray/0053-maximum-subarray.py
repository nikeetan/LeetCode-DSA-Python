'''
maxi = 0
p1 = 0 
p2 = 0
current_sum = 0                                         [5, 4 , -1 , 7, 8]
for p1 in range(len(nums)):         o(n)                                p1
    for p2 in range(p1,len(nums)):  o(n)                 23 23  23  23  23
        current_sum += nums[p2]                          # 
        maxi = max(maxi, current_sum) tc : o(n**2), sc : o(1)
return maxi

'''

'''                          [-2,1,-3,4,-1,2,1,-5,4]
ans = float('-inf')          ans = - Null
curr_sum = 0                    
for i in range(len(nums)):    
    curr_sum = max(nums[i], nums[i]+curr_sum
    ans = max(ans , curr)   
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')          
        curr_sum = 0                    
        for i in range(len(nums)):    
            curr_sum = max(nums[i], nums[i]+curr_sum)
            ans = max(ans , curr_sum) 
        return ans  