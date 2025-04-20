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
        # indx = 0
        # res = []
        # # Finding overlapping interval
        # while ((indx < len(intervals)) and (intervals[indx][1] < newInterval[0])):
        #     res.append(intervals[indx])
        #     indx += 1
        
        # #Merging
        # while indx < len(intervals) and newInterval[1] >= intervals[indx][0]:
        #     # minimum of start
        #     newInterval[0] = min(intervals[indx][0], newInterval[0])
        #     # maximum of end
        #     newInterval[1] = max(intervals[indx][1], newInterval[1])
        #     indx += 1
        # res.append(newInterval)
        
        # # adding the remaining:
        # while indx < len(intervals):
        #     res.append(intervals[indx])
        #     indx += 1
        # return res

        res = []
        # first we wil find the position to insert the new interval through bs why bs bcz iuntervals are sorted
        left, right = 0 , len(intervals) - 1
        while left <= right:
            mid = left + (right - left)//2
            if intervals[mid][0] > newInterval[0]:
                right = mid - 1
            else:
                left = mid + 1
        
        # check bs works and needs any improvements
        intervals.insert(left, newInterval)
        print(intervals)
        # now adding one by one
        for interval in intervals:
            
            if len(res) == 0:
                res.append(interval)
            elif res[-1][-1] >= interval[0]:
                res[-1][0] = min(res[-1][0], interval[0])
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res
            


        return []
