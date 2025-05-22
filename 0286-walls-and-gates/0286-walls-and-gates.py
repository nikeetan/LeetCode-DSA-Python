'''
- 1 obstacle
0 A gate
'''

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        visited = set()
        queue = deque()
        R = len(rooms)
        C = len(rooms[0])
        directions = [(0, -1),(0, 1),(-1, 0), (1, 0)]
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    queue.append((0, r, c))

        while queue:
            dist , row , col = queue.popleft()
            rooms[row][col] = dist
            for offset_x, offset_y in directions:
                new_row = row + offset_x
                new_col = col + offset_y

                if ((new_row < 0 or new_row >= R) or(new_col < 0 or new_col >= C)) or rooms[new_row][new_col] == -1 or rooms[new_row][new_col] == 0 or (new_row, new_col) in visited :
                    continue
                queue.append((dist + 1 , new_row, new_col))
                visited.add((new_row, new_col))
        
                
        
                
        


