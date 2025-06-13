class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # if i need to run a computer for 5 mins i require battery power 5
        # if i need to run a computer for 10 mins i require battery power 10
        # if i need to run 2 computers for 5 min then i require battery power 10
        # if i need to run 3 computers for 5 min then i require battery power 15
        total_capacity = sum(batteries)
        def ispossible(time):
            power = 0
            for capacity in batteries:
                power += min(capacity, time) # lets say i have capacity 3 and time 5 i will utilize all , when i have time 3 capacity to be 5 i will utilize till 3
            if power >= time * n:
                return True
            return False

        l, r = 1, (total_capacity) // n
        ans = 1
        while l <= r:
            mid = l + (r - l) // 2
            if ispossible(mid):
                #print(mid, l , r)
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans



