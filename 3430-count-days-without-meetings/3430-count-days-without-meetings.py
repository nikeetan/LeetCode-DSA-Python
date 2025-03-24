class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)
        days_available = 0
        previous_end = 0
        for start,end in meetings:
            if start > previous_end + 1:
                days_available += (start - (previous_end + 1))
            previous_end = max(previous_end, end)        
        days_available += (days - previous_end)
        return days_available

