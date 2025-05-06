class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        Brute force is traverse using two loops and find the % if they are equal to j - i + 1 >= 2 then 
        and take the subarray sum and check divisible by k
        return True
        TC : O(n3)
        SC : O(1)
        '''

        '''
        intution when we have 
        [23,2,4,6,7]
        23 % 6 = 5
        25 % 6 = 1 
        29 % 6 = 5
        we can see we started with the remainder 5 and we ended up with the same remainder that means to the first number there is some added which is the multiple of k so we will return true

        '''
        hash_map = {0 : -1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix % k in hash_map:
                if (i - hash_map[prefix % k]) > 1:
                    return True
            else:
                hash_map[prefix % k] = i

        return False

        #25 6