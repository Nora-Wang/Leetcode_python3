You are given a m x n matrix grid consisting of non-negative integers where grid[row][col] represents the minimum time required to be able to visit the cell (row, col), which means you can visit the cell (row, col) only when the time you visit it is greater than or equal to grid[row][col].

You are standing in the top-left cell of the matrix in the 0th second, and you must move to any adjacent cell in the four directions: up, down, left, and right. Each move you make takes 1 second.

Return the minimum time required in which you can visit the bottom-right cell of the matrix. If you cannot visit the bottom-right cell, then return -1.

 

Example 1:



Input: grid = [[0,1,3,2],[5,1,2,5],[4,3,8,6]]
Output: 7
Explanation: One of the paths that we can take is the following:
- at t = 0, we are on the cell (0,0).
- at t = 1, we move to the cell (0,1). It is possible because grid[0][1] <= 1.
- at t = 2, we move to the cell (1,1). It is possible because grid[1][1] <= 2.
- at t = 3, we move to the cell (1,2). It is possible because grid[1][2] <= 3.
- at t = 4, we move to the cell (1,1). It is possible because grid[1][1] <= 4.
- at t = 5, we move to the cell (1,2). It is possible because grid[1][2] <= 5.
- at t = 6, we move to the cell (1,3). It is possible because grid[1][3] <= 6.
- at t = 7, we move to the cell (2,3). It is possible because grid[2][3] <= 7.
The final time is 7. It can be shown that it is the minimum time possible.
Example 2:



Input: grid = [[0,2,4],[3,2,1],[1,0,4]]
Output: -1
Explanation: There is no path from the top left to the bottom-right cell.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
0 <= grid[i][j] <= 105
grid[0][0] == 0



# Dijkstra
# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/discuss/6093176/Python-or-Greedy-pattern-and-Shortest-Path-(Dijkstra)
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        # min_heap, which means everytime when heappop, it will popup the cell with minimum time
        heap = [(0, 0, 0)]
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        # visite cell for only once
        visited = set()
        visited.add((0,0))
        
        while heap:
            time, x, y = heapq.heappop(heap)

            # end case
            if x == m - 1 and y == n - 1:
                return time
            
            for d_x, d_y in direction:
                x_, y_ = x + d_x, y + d_y
                
                if not self.isValid(grid, x_, y_, visited):
                    continue

                # Case 1: current grid value is smaller than time + 1
                if grid[x_][y_] <= time + 1:
                    heapq.heappush(heap, (time + 1, x_, y_))
                else:
                    # Even if a cell can't be visited at the current time, its fine to visit later. 
                    # Instead of passing the cell and potentially backtracking until time allows you to enter, 
                    # it's more efficient to add the cell to the heap for when you can visit the node, no backtracking needed.
                    gap = grid[x_][y_] - time
                    # gap is the waiting time before you can enter the cell. Need to know if gap is odd or even to know timing of when can enter.
                    # If gap is even, then you can't enter the cell at cell time and need to add 1 to cell time.
                    if gap % 2 == 0:
                        heapq.heappush(heap, (grid[x_][y_] + 1, x_, y_))
                    else:
                        # If the gap is odd, then you can enter the cell at cell time.
                        heapq.heappush(heap, (grid[x_][y_], x_, y_))
                        
                visited.add((x_,y_))
        
        return -1
    
    def isValid(self, grid, x, y, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        
        if (x,y) in visited:
            return False
        
        return True
                


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        m, n = len(grid), len(grid[0])
        heap = [(0, 0, 0)]
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()
        visited.add((0,0))
        
        while heap:
            time, x, y = heapq.heappop(heap)
            
            if x == m - 1 and y == n - 1:
                return time
            
            for d_x, d_y in direction:
                x_, y_ = x + d_x, y + d_y
                
                if not self.isValid(grid, x_, y_, visited):
                    continue
                
                # Simplify the gap calculation method
                wait = 1 if abs(grid[x_][y_] - time) % 2 == 0 else 0
                new_time = max(grid[x_][y_] + wait, time + 1)
                    
                heapq.heappush(heap, (new_time, x_, y_))
                visited.add((x_,y_))
        
        return -1
    
    def isValid(self, grid, x, y, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        
        if (x,y) in visited:
            return False
        
        return True
                
