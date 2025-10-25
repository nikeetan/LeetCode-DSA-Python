class solution:
    def find_path(self, matrix) -> list[(int, int)]:
        R = len(matrix)
        C = len(matrix[0])
        r, c = 0, 0
        visited = set()
        path = []
        def helper(matrix, r, c):
            # Base condition
            nonlocal path
            if r == R - 1 and c == C - 1:
                if matrix[r][c] == 1:
                    path.append((r, c))
                    return True
                return False
                
            if ((r < 0 or r >= R) or (c < 0 or c >= C)):
                return False
            if matrix[r][c] == 1:
                path.append((r, c))
                # Moving right
                if helper(matrix, r , c + 1):
                    return True
                # Moving down
                if helper(matrix, r + 1, c):
                    return True
                path.pop()
            return False
        if helper(matrix, r, c):
            return path
        return -1
    


matrix = [[1, 1, 1, 1, 0], 
          [0, 1, 0, 0, 0], 
          [0, 1, 1, 1, 0], 
          [0, 0, 0, 1, 0],
          [1, 1, 1, 1, 1] 
          ]
fetch = solution()
print(fetch.find_path(matrix))









