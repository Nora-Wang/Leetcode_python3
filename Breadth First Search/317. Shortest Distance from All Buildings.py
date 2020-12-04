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



'''
shortest distance -> BFS
start from every building to find out the shortest distance from every building '1' to every empty land '0'
-> empty_to_building = {empty_land_position:[total_distance_to_buildings, reached_building_count]}
based on empty_to_building to find out the result

queue: BFS
visited: avoid repeated traverse

time: O(number_1 * n*m) = worse case O(n*m * n*m)
space: O(n*m)

Questions:
1. why not from every empty land '0' to do the BFS?
starting from '0' will repeated computation for every same path positions, if without memorization

2. for the grid below, what's the diff for start from '0' and '1'?
[[1, 1, 1, 1, 1],
 [0, 0, 0, 0, 0],
 [1, 1, 1, 1, 1],
 [0, 0, 0, 0, 0],
 [1, 1, 1, 1, 1]]
 they are actually the same, both start from '0' and '1' cannot pass through buildings -> both will return -1 

'''
# Grid version
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        
        distance = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        reached = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        building_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, distance, reached)
                    building_count += 1
                    
        res = float('inf')
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and distance[i][j] < res and reached[i][j] == building_count:
                    res = distance[i][j]
        
        return res if res != float('inf') else -1
                    
    def bfs(self, grid, x, y, distance, reached):
        visited = set()
        visited.add((x,y))
        queue = collections.deque([(x,y)])
        step = 0
        
        while queue:
            step += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                
                for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x_ = x + direct[0]
                    y_ = y + direct[1]
                    
                    if self.is_valid(grid, x_, y_, visited):
                        queue.append((x_,y_))
                        visited.add((x_,y_))
                        distance[x_][y_] += step
                        reached[x_][y_] += 1
        
    def is_valid(self, grid, x, y, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        
        if grid[x][y] != 0:
            return False
        
        if (x,y) in visited:
            return False
        
        return True
            

# Hashtable version
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        
        empty = {} # {position:(total distance to buildings, reached buildings count)}
        building_count = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j, empty)
                    building_count += 1
                    
        res = float('inf')
        for e in empty:
            if empty[e][0] < res and empty[e][1] == building_count:
                res = empty[e][0]
        
        return res if res != float('inf') else -1
                    
    def bfs(self, grid, x, y, empty):
        visited = set()
        visited.add((x,y))
        queue = collections.deque([(x,y)])
        distance = 0
        
        while queue:
            distance += 1
            for _ in range(len(queue)):
                x,y = queue.popleft()
                
                for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x_ = x + direct[0]
                    y_ = y + direct[1]
                    
                    if self.is_valid(grid, x_, y_, visited):
                        queue.append((x_,y_))
                        visited.add((x_,y_))
                        if (x_,y_) in empty:
                            empty[(x_,y_)][0] += distance
                            empty[(x_,y_)][1] += 1
                        else:
                            empty[(x_,y_)] = [distance, 1]
        
    def is_valid(self, grid, x, y, visited):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        
        if grid[x][y] != 0:
            return False
        
        if (x,y) in visited:
            return False
        
        return True
            
        
        




















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
    
