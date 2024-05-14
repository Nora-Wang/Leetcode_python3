In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

# 2024/05/14
# dfs
# Time O(n*m), Space O(n*m)
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        queue = collections.deque([(0,0)])
        self.res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.dfs(grid, i, j, set(), 0)
        
        return self.res
    
    def dfs(self, grid, x, y, visited, cur):
        if self.isInvalid(grid, x, y, visited):
            self.res = max(self.res, cur)
            return
        
        cur += grid[x][y]
        visited.add((x, y))
        
        for move_x,move_y in [(0,1),(1,0),(-1,0),(0,-1)]:
            next_x, next_y = x + move_x, y + move_y
            
            self.dfs(grid, next_x, next_y, visited, cur)
            
        visited.remove((x, y))
        
        return
            
    def isInvalid(self, grid, x, y, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return True
        
        if grid[x][y] == 0:
            return True
        
        if (x,y) in visited:
            return True
        
        return False


# DFS optimized for Space
# Time O(n*m), Space O(1)
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        queue = collections.deque([(0,0)])
        self.res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    self.dfs(grid, i, j, 0)
        
        return self.res
    
    def dfs(self, grid, x, y, cur):
        if self.isInvalid(grid, x, y):
            self.res = max(self.res, cur)
            return
        
        cur += grid[x][y]
        record = grid[x][y]
        grid[x][y] = 0
        
        for move_x,move_y in [(0,1),(1,0),(-1,0),(0,-1)]:
            next_x, next_y = x + move_x, y + move_y
            
            self.dfs(grid, next_x, next_y, cur)
            
        grid[x][y] = record
        
        return
            
    def isInvalid(self, grid, x, y):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return True
        
        if grid[x][y] == 0:
            return True
        
        return False








DFS


code:
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        self.res = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                    
                curt_max_sum = self.dfs(grid, i, j, 0, set())
                self.res = max(self.res, curt_max_sum)
    
        return self.res
    
    def dfs(self,grid, x, y, sum_record, visited):
        if not self.check(grid, x, y, visited):
            return sum_record
        
        visited.add((x,y))
        sum_record += grid[x][y]
        
        #四个方向得到一个当前的最大和
        sum_record = max(self.dfs(grid, x+1, y, sum_record, visited), \
                       self.dfs(grid, x-1, y, sum_record, visited), \
                       self.dfs(grid, x, y+1, sum_record, visited), \
                       self.dfs(grid, x, y-1, sum_record, visited))
        
        visited.remove((x, y))
        
        return sum_record
                
    def check(self, grid, x, y, visited):
        if 0 > x or x >= len(grid) or 0 > y or y >= len(grid[0]):
            return False
        
        if (x, y) in visited:
            return False
        
        if grid[x][y] == 0:
            return False
        
        return True
                
