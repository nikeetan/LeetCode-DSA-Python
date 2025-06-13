class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def ispossible(threshold):
            # Greedy
            indx = 1
            valid_pair_cnt = 0
            while indx < len(nums):
                if nums[indx] - nums[indx - 1] <= threshold:
                    valid_pair_cnt += 1
                    indx += 2
                else:
                    indx += 1
                if valid_pair_cnt >= p:
                    return True
            return False
        l, r = 0, nums[-1] - nums[0]
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if ispossible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans 
                
