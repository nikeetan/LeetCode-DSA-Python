class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        '''
        nums_set = list(set(nums))
        max_count = 0
        for num in nums:
            count=1
            while num*num in nums_set:
                num = num*num
                count+=1
            max_count = max(max_count,count)
        if max_count ==1:
            return -1
        else:
            return max_count
        '''
        nums.sort()
        mp = {}
        res = -1
        for num in nums:
            sqrt = isqrt(num)
            if sqrt * sqrt == num and sqrt in mp:
                mp[num]=mp[sqrt]+1
                res = max(res,mp[num])
            else:
                mp[num]=1
        return res

