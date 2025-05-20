class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
                                                        # triptime, count 
        self.stations = collections.defaultdict(lambda : [0 , 0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.checkin:
            self.checkin [id] = (stationName, t)
    
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.checkin:
            start_station, start_time = self.checkin[id]
            self.stations[(start_station, stationName)][0] += (t - start_time)
            self.stations[(start_station, stationName)][1] += 1
            self.checkin.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.stations[(startStation, endStation)][0] / self.stations[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)