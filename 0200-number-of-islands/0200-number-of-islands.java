class Pair{
    int row, col; 
    Pair(int row, int col){
        this.row = row;
        this.col = col;
    }
}
class Solution {
    private static int [][] directions = {{-1, 0},{1, 0}, {0, -1},{0, 1}};
    public static char[][] bfs(int r, int c, char [][] grid, int R, int C){
        Deque<Pair> queue = new ArrayDeque<>();
        queue.add(new Pair(r, c));
        grid[r][c] = '0';
        while (!queue.isEmpty()){
            Pair currDirections = queue.removeFirst();
            for(int [] newDirections : directions){
                Pair offset = new Pair(0, 0);
                offset.row = currDirections.row + newDirections[0];
                offset.col = currDirections.col + newDirections[1];
                if (((0 <= offset.row) && (offset.row< R))
                && ((0 <= offset.col) && ( offset.col < C))
                 && (grid[offset.row][offset.col] == '1'))
                {
                    queue.add(new Pair(offset.row, offset.col));
                    grid[offset.row][offset.col] = '0';
                }
            }

        }
        return grid;
    }
    public int numIslands(char[][] grid) {
        int R = grid.length;
        int C = grid[0].length;
        int islandCount = 0;
        for(int r = 0; r < R; r ++){
            for(int c = 0; c < C; c ++){
                if(grid[r][c] == '1'){
                    grid = bfs(r, c, grid, R, C);
                    islandCount += 1;
                }
            }
        }
        return islandCount;
    }
}