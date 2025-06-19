class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        queens = []
        posDiag = set()
        negDiag = set()
        col = set()
        def helper(row):
            # edge case 
            if row == n:
                part_res = []
                for row in board:
                    part_res.append(''.join(row[:]))
                queens.append(part_res)
                return 
            for curr_col in range(n):
                if ((curr_col in col) or ((row + curr_col) in posDiag) or ((row - curr_col) in negDiag)):
                    continue
                col.add(curr_col)
                posDiag.add(row + curr_col)
                negDiag.add(row - curr_col)
                board[row][curr_col] = 'Q'

                helper(row + 1)

                col.remove(curr_col)
                posDiag.remove(row + curr_col)
                negDiag.remove(row - curr_col)
                board[row][curr_col] = '.'
        helper(0)
        return queens
            



            

                