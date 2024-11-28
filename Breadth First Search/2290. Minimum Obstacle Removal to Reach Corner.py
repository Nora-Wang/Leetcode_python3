You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).

 

Example 1:


Input: grid = [[0,1,1],[1,1,0],[1,1,0]]
Output: 2
Explanation: We can remove the obstacles at (0, 1) and (0, 2) to create a path from (0, 0) to (2, 2).
It can be shown that we need to remove at least 2 obstacles, so we return 2.
Note that there may be other ways to remove 2 obstacles to create a path.
Example 2:


Input: grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]
Output: 0
Explanation: We can move from (0, 0) to (2, 4) without removing any obstacles, so we return 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
2 <= m * n <= 105
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 0



# DFS - TLE
  class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        
        n, m = len(grid), len(grid[0])
        
        self.res = n * m
        visited = set()
        visited.add((0,0))
        # pruning - if current count for [x,y] is larger than previous path, then, don't need to dive deep anymore.
        self.record = [[n*m for _ in range(m)] for _ in range(n)]
        
        self.dfs(grid, visited, 0, 0, 0)
        
        return self.res
    
    def dfs(self, grid, visited, count, x, y):
        if grid[x][y] == 1:
            count += 1
            
        if self.record[x][y] <= count:
            return
        
        self.record[x][y] = min(self.record[x][y], count)
        
        if x == len(grid) - 1 and y == len(grid[0]) - 1:
            self.res = min(self.res, count)
            return
        
        for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
            x_next, y_next = x + i, y + j
            
            if not self.isValid(grid, x_next, y_next, visited):
                continue
            
            visited.add((x_next, y_next))
            self.dfs(grid, visited, count, x_next, y_next)
            visited.remove((x_next, y_next))
            
    
    def isValid(self, grid, x, y, visited):
        if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
            return False
        
        if (x, y) in visited:
            return False
        
        return True


# BFS
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        
        m, n = len(grid), len(grid[0])
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        
        queue = collections.deque([(0,0,0)])
        while queue:
            x, y, count = queue.popleft()
            
            if x == m - 1 and y == n - 1:
                return count
            
            for i,j in direction:
                x_next, y_next = x + i, y + j
                
                if 0 <= x_next < m and 0 <= y_next < n and not visited[x_next][y_next]:
                    visited[x_next][y_next] = True
                    if grid[x_next][y_next] == 0:
                        queue.appendleft((x_next, y_next, count))
                    else:
                        queue.append((x_next, y_next, count + 1))
        
        return -1
