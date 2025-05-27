class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        dp
        '''
        '''
        dp = [1 for _ in range(len(nums))]
        ans = float("-inf")
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(ans, dp[i])
        return ans
        '''
        '''
        swap like have the increasing oreder if curr_num is greater than the sub num then append to the sub array else what i will do is find the point where the element in sub is greater than current_num then swap
        '''

        '''
        find position of the new element to be inserted into sub if that is equal to the len(sub) just append it otherwise swap number to the following index
        '''

        def search_pos(sub, number):
            l, r = 0, len(sub) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if sub[mid] == number:
                    return mid
                elif number < sub[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l
        sub = []
        for num in nums:
            indx = search_pos(sub, num)
            if indx == len(sub):
                sub.append(num)
            else:
                sub[indx] = num
        return len(sub)



         
        