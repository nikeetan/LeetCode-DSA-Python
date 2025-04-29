class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])

        # first i need to make the boundaries reching the atlantic and pacific ocean
        atl, pac = set(), set()

        # figure out which are the ones that will reach atlantic ocean and which are the ones that will reach pacific for rows and columns 
        def dfs(r, c , visited, prev_height):
            # check for out of bounds
            if (r,c) in visited or ((r < 0) or (c < 0)) or ((r >= row) or (c >= col)) or (prev_height > heights[r][c]):
                return
            visited.add((r,c))

            dfs (r - 1, c, visited, heights[r][c])
            dfs (r + 1, c, visited, heights[r][c])
            dfs (r, c + 1, visited, heights[r][c])
            dfs (r, c - 1, visited, heights[r][c])
        
        # we should now add the col part for the atlantic and pacific that is for the first row and last row
        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row - 1, c, atl, heights[row - 1 ][c])
  
        # we should now be adding the col part that is first col and the last col

        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col - 1, atl, heights[r][col - 1])

        # now check the common in both of the ocean sets
        res = []
        for (r, c)  in atl:
            if (r,c) in pac:
                res.append((r, c))
        return res
            

