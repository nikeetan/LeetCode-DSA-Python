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


'''

maxi = -infc
curr_sum = 0
[-2,1,-3,4,-1,2,1,-5,4]

Itr1 
curr_sum = -2
maxi = (-inf, -2) 

Itr2
curr_sum = -1
maxi = (-2, -1)

Itr3
curr_sum = -4
maxi = (-1, -4)

Itr4
curr_sum = 0
maxi = (-1, 0)

Itr5
curr_sum = -1
maxi = (0, -1)

Itr6
curr_sum = 1
maxi = (0, 1)

Itr7
curr_sum = 2
maxi = (1, 2)

Itr8
curr_sum = -3
maxi = (2, -3)

Itr9
curr_sum = 6
maxi = (2, 6)



o(n)
o(1)
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        subMax = float('-inf')
        for currnum in nums:
            currSum += currnum
            currSum = max(currSum, currnum)
            subMax = max(subMax, currSum)
        return subMax
    



