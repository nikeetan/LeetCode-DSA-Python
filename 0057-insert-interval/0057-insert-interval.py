'''
in the first pass we can find which is that interval i can merge like
[1, 3], [6, 9]
[1, 5], [6, 9]
 in the next pass i will order the intervals accordingly
[1,2],[3,8],[6,7],[8,10],[12,16]


i will check if prev > start

[1, 2], [3, 8] 

false
3, 10 



'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        three senarios
        current interval ends before the start of new interval

        overalapp interval needs merging

        current interval starts after the new interval ends
        '''
        indx = 0
        res = []
        # Finding overlapping interval
        while ((indx < len(intervals)) and (intervals[indx][1] < newInterval[0])):
            res.append(intervals[indx])
            indx += 1
        
        #Merging
        while indx < len(intervals) and newInterval[1] >= intervals[indx][0]:
            # minimum of start
            newInterval[0] = min(intervals[indx][0], newInterval[0])
            # maximum of end
            newInterval[1] = max(intervals[indx][1], newInterval[1])
            indx += 1
        res.append(newInterval)
        
        # adding the remaining:
        while indx < len(intervals):
            res.append(intervals[indx])
            indx += 1
        return res
