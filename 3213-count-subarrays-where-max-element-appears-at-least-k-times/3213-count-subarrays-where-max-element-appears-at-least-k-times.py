class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        '''
        find the max ele
        '''

        '''
        max_ele = max(nums)
        l, r = 0 , 0
        max_count = 0
        sub_array_cnt = 0
        while r < len(nums):
            if nums[r] == max_ele:
                max_count += 1 
            while max_count == k:
                if nums[l] == max_ele:
                    max_count -= 1
                l += 1
            sub_array_cnt += l
            r += 1
        return sub_array_cnt
        '''
        # through index
        max_ele = max(nums)
        max_indx = []
        valid_sub = 0
        for r in range(len(nums)):
            if nums[r] == max_ele:
                max_indx.append(r)
           
            if len(max_indx) >= k:
                valid_sub += max_indx[-k] + 1
        return valid_sub


