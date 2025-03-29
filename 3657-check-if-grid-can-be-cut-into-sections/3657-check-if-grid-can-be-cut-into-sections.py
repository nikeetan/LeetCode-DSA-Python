class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        '''
        Intial idea to sort startx and endy grouping and then sorting them basically by this 
        '''
        horizontal = []
        vertical = []
        for startx,starty,endx,endy in rectangles:
            horizontal += [[starty, endy]]
            vertical += [[startx, endx]]
        horizontal = sorted(horizontal)
        vertical = sorted(vertical)

        previous_end = -1
        count_partitions = 0
        for start, end in horizontal:
            if start >= previous_end:
                count_partitions += 1
            previous_end = max(end, previous_end)
        if count_partitions >= 3:
            return True

        previous_end = -1
        count_partitions = 0
        for start, end in vertical:
            if start >= previous_end:
                count_partitions += 1
            previous_end = max(end, previous_end)
        if count_partitions >= 3:
            return True
        return False