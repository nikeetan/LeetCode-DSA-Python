class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        if len(intervals) > 1:
            prev_end = intervals[0][-1]
            for i in range(1, len(intervals)):
                
                if intervals[i][0] < prev_end:
                    return False
                prev_end = intervals[i][-1]
            return True
        else:
            return True
