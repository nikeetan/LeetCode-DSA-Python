import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        duration_heap = []
        intervals.sort()
        meeting_room = 0
        # Now check for a current meeting start is there any room available which has completed
        for i in intervals:
# checking my end time of the minimum duration meeting is lesser than the current start 
            if duration_heap:
                if duration_heap[0] <= i[0]:
                    # i have used the room and set a new duration
                    heapq.heappop(duration_heap)
            heapq.heappush(duration_heap, i[1])
        return len(duration_heap)
