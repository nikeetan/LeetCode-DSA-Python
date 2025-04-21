class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def ispossible(k):
            hours = 0
            for bananas in piles:
                hours = hours + math.ceil(bananas/k)

            if hours <= h:
                return True
            return False
    
        low, high = 1, max(piles)
        ans = -1
        while low <= high:
            mid = low + (high - low)//2
            if ispossible(mid):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1
        return ans