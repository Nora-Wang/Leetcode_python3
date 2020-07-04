You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
Example:

Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

Output: 7 

Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2),
             the point (1,2) is an ideal empty land to build a house, as the total 
             travel distance of 3+3+1=7 is minimal. So return 7.
Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.


参考Lintcode 573


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return -1
        
        building = set()
        obstacle = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    building.add((i,j))
                elif grid[i][j] == 2:
                    obstacle.add((i,j))
        
        #use a hash table to record how many buildings can reach this empty land
        b_count_r = {}
        for x, y in building:
            #from every building to count the distance from them to every empty land
            self.bfs(grid, x, y, building, obstacle, b_count_r)
        
        res = float('inf')
        for p in b_count_r:
            if b_count_r[p] != len(building) or p in building or p in obstacle:
                continue
            res = min(res, grid[p[0]][p[1]])
        
        #if there has no empty land match the requirment -> return -1
        return res if res != float('inf') else -1
    
    def bfs(self, grid, x, y, building, obstacle, b_count_r):
        queue = collections.deque([(x,y)])
        visited = set()
        step = 0
        
        while queue:
            step += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                for direct in [(0,1), (0,-1), (1,0), (-1,0)]:
                    x_, y_ = x + direct[0], y + direct[1]
                    
                    if self.check(grid, x_, y_, building, obstacle, visited):
                        queue.append((x_,y_))
                        grid[x_][y_] += step
                        visited.add((x_,y_))
                        b_count_r[(x_,y_)] = b_count_r.get((x_,y_), 0) + 1
        
        return

    def check(self, grid, x, y, building, obstacle, visited):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        
        if (x,y) in building or (x,y) in obstacle or (x,y) in visited:
            return False
        
        return True
    
