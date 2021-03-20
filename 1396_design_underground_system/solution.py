class UndergroundSystem:

    def __init__(self):
        """
        {
            src: {
                dest: {
                    numJourneys: int
                    totalTime: int
                }
            }
        }
        """
        self.journeys = {}
        self.ongoing_journey = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ongoing_journey[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        src, entry_t = self.ongoing_journey[id]
        if not src in self.journeys:
            self.journeys[src] = {}
            self.journeys[src][stationName] = collections.defaultdict(int)
        elif not stationName in self.journeys[src]:
            self.journeys[src][stationName] = collections.defaultdict(int)
        self.journeys[src][stationName]["numJourneys"] += 1
        self.journeys[src][stationName]["totalTime"] += t - entry_t

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if not (self.journeys.get(startStation) and self.journeys[startStation].get(endStation)):
            return 0
        details = self.journeys[startStation][endStation]
        numJ = details["numJourneys"]
        if not numJ:
            return 0
        return details["totalTime"]/numJ

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
