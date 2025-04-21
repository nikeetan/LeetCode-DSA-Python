class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def ispossible(time):
            car_count = 0
            for i in range(len(ranks)):
                car_count += int(math.sqrt(time/ranks[i]))
                if car_count >= cars:
                    return True
            return False
            

        low , high = 1,  max(ranks) * cars * cars
        ans = - 1
        while low <= high:
            mid = low + (high - low)//2
            if ispossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans