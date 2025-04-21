class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
       
        def ispossible(capacity):
            day_count = 1
            curr_load = 0
            for i in range(len(weights)):
                curr_load += weights[i]
                if curr_load > capacity:
                    day_count += 1
                    curr_load = weights[i]
                    if day_count > days:
                        return False
            return day_count <= days

        
        low , high = max(weights), sum(weights)
        ans = -1
        while low <= high:
            mid = low + (high - low)//2
            if ispossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1 
        
        return ans


