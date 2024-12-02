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


# Dijkstra
# time O(nm \log(nm)), space O(nm)
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        heap = [(0,0,0)]
        visited = set()
        visited.add((0,0))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        
        while heap:
            obs, x, y = heapq.heappop(heap)
            
            if x == len(grid) - 1 and y == len(grid[0]) - 1:
                return obs
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if not self.isValid(grid, nx, ny, visited):
                    continue

                # Do not change obs directly, it will impact the obs value in next directions for loop
                heapq.heappush(heap, (obs + grid[nx][ny], nx, ny))
                visited.add((nx,ny))
                
        return 0
    
    def isValid(self, grid, x, y, visited):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        
        if (x,y) in visited:
            return False
        
        return True
