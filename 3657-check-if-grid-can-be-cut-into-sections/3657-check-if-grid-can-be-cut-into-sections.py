class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        horizontal = []
        vertical = []
        for startx,starty,endx,endy in rectangles:
            horizontal += [[starty, endy]]
            vertical += [[startx, endx]]
        horizontal = sorted(horizontal)
        vertical = sorted(vertical)

        def count_partitons(coordinates):
            previous_end = -1
            count = 0
            for start, end in coordinates:
                if start >= previous_end:
                    count += 1
                previous_end = max(end, previous_end)
            return count
        return max(count_partitons(horizontal),count_partitons(vertical)) >=3