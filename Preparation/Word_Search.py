'''
idea is i am thinking of implementing trie and then searching why trie because 
evaluates the next index soon like we can think of if we have multiple words 
rather revisiting the grid everytime if i am able to get the word from the same
path i would be having one dfs call fetching multiple words at a time
'''
class Solution:
    def __init__(self):
        self.directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    def dfs(self , R, C, board, row, col, word, indx):
        print("Index", indx)
        if indx == len(word):
            return True
        for dir_x, dir_y in self.directions:
            new_row, new_col = row + dir_x, col + dir_y
            if ((0 <= new_row <R) and (0 <= new_col < C)):
                print("(row, col)",(new_row, new_col))
                if board[new_row][new_col] == word[indx]:
                    temp = board[new_row][new_col]
                    board[new_row][new_col] = '#'
                    if self.dfs(R, C, board, new_row, new_col, word, indx + 1):
                        return True
                    board[new_row][new_col] = temp
        return False

    def exist(self,board: list[list[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        indx = 0
        for row in range(R):
            for col in range(C):
                if board[row][col] == word[indx]:
                    # temp = board[row][col]
                    # board[row][col] = '#'
                    if self.dfs(R, C, board, row, col, word, indx + 1):
                        return True
                    # board[row][col] = temp
        return False
        





word_find = Solution()
board =[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "AA"
print(word_find.exist(board, word))

# [N I C E
#  F K E S 
#  T D A N]

