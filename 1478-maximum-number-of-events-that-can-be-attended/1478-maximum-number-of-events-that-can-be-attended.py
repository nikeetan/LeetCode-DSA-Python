class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events = sorted(events,key = lambda x : (x[0],x[1]))
        max_day = max(x[1] for x in events)
        min_heap = []
        events_attended = 0
        indx = 0
        for day in range(1, max_day+1):
            while (indx < len(events)) and  events[indx][0] <= day:
                heapq.heappush(min_heap, events[indx][1])
                indx += 1
            
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                events_attended += 1


        return events_attended