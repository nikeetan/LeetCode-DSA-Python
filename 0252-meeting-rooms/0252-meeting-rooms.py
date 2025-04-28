class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals.sort()
        if len(intervals) > 1:
            prev_end = intervals[0][-1]
            for i in range(1, len(intervals)): 
                if intervals[i][0] < prev_end:
                    return False
                prev_end = intervals[i][-1]
            return True
        else:
            return True
        # Time complexity is 
        # O(n log n) for sorting
        # and for traversing O (n)
        # so total will be o(n logn) + o(n)
        # since o(n logn ) will be dominant my total time complexity would be o(n logn)
        # Space complexity = O(1) no extra space is being used
