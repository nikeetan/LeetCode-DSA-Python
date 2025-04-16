class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
       
        buses = sorted(buses)
        psng = sorted(passengers)
        psng_set = set(passengers)
        indx = 0
        for bus in buses:
            count = 0
            # how many psng could be in following bus
            while indx < len(psng) and count < capacity and psng[indx] <= bus:
                indx += 1
                count += 1

        if count < capacity:
            latest = bus
        else:
            latest = psng[indx - 1] - 1 

        while latest in psng_set:
            latest -= 1 
        return latest