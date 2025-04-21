class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def ispossible(speed):
            time_taken = 0
            for i in range(len(dist)):
                if i <= len(dist) - 2:
                    time_taken += math.ceil(dist[i]/speed)
                else:
                    time_taken += dist[i]/ speed
                
            if time_taken <= hour:
                return True
            else:
                return False
        l, r = 1, 1000000000
        ans = -1
        while l <= r:
            mid = l + (r - l)//2
            if ispossible(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans


