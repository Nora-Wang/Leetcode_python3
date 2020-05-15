Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).


code:
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not len(matrix) or not len(matrix[0]):
            return []
        
        n, m = len(matrix), len(matrix[0])
        
        p_visited = [[False for _ in range(m)] for _ in range(n)]
        a_visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            self.dfs(matrix, i, 0, p_visited, n, m)
            self.dfs(matrix, i, m-1, a_visited, n, m)
        
        for j in range(m):
            self.dfs(matrix, 0, j, p_visited, n, m)
            self.dfs(matrix, n-1, j, a_visited, n, m)
            
        res = []
        for i in range(n):
            for j in range(m):
                if p_visited[i][j] and a_visited[i][j]:
                    res.append([i,j])
        
        return res
    
    def dfs(self, matrix, x, y, visited, n, m):
        visited[x][y] = True
        
        for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
            x_, y_ = direct[0] + x, direct[1] + y
            
            if 0 <= x_ < n and 0 <= y_ < m and matrix[x_][y_] >= matrix[x][y] and not visited[x_][y_]:
                self.dfs(matrix, x_, y_, visited, n, m)
