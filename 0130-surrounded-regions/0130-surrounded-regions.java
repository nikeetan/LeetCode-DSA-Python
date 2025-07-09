class Pair{
    int row, col;
    Pair(int row, int col){
        this.row = row;
        this.col = col;
    }
}

class Solution {

    private int [][] directions = {{-1, 0},{1, 0},{0, -1}, {0, 1}};
    public void bfs(char [][] board, int R, int C){

        Deque<Pair> queue = new ArrayDeque<>();
        for(int r = 0; r < R; r++){
            for(int c = 0; c < C; c ++){
                if (((r == 0 || r == R - 1) || (c == 0 || c == C - 1)) && board[r][c] == 'O'){
                    queue.add(new Pair(r, c));
                }

            }
        }
        while(!queue.isEmpty()){
            Pair coordinates = queue.removeFirst();
            if (board[coordinates.row][coordinates.col] == 'O'){
                board[coordinates.row][coordinates.col] = 'T';
            }
            for(int [] offset : directions){
                int newX = coordinates.row + offset[0]; 
                int newY = coordinates.col + offset[1]; 

                if(((newX >= 0 && newX < R) && (newY >= 0 && newY < C)) && (board[newX][newY] == 'O')){
                    queue.add(new Pair(newX, newY));
                }
            }
        }
    }
    public void solve(char[][] board) {

        int R = board.length;
        int C = board[0].length;

        bfs(board, R, C);

        for(int r = 0; r < R; r++){
            for(int c = 0; c < C; c ++){
                if (board[r][c] == 'O'){
                    board[r][c] = 'X';
                }
                else if(board[r][c] == 'T'){
                    board[r][c] = 'O';
                }
            }
        }

    }
}
