You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
  

#07/03/2020
#BFS
#time: O(n), space: O(n). n = all the elements in grid
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not len(rooms) or not len(rooms[0]):
            return
        
        n, m = len(rooms), len(rooms[0])
        
        queue = collections.deque()
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    queue.append((i, j))
        
        while queue:
            x, y = queue.popleft()

            for direct in [(0,1), (0,-1), (1,0), (-1,0)]:
                x_, y_ = x + direct[0], y + direct[1]

                if self.check(rooms, x_, y_):
                    rooms[x_][y_] = rooms[x][y] + 1
                    queue.append((x_, y_))
        
        return
    
    def check(self, rooms, x, y):
        if x < 0 or x >= len(rooms) or y < 0 or y >= len(rooms[0]):
            return False
        
        if rooms[x][y] != 2 ** 31 - 1:
            return False
        
        return True
  
  
#DFS
#time: O(n^2), space: O(1). n = all the elements in grid
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not len(rooms) or not len(rooms[0]):
            return
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j)
        
        return 
    
    def dfs(self, rooms, x, y):
        for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
            x_, y_ = x + direct[0], y + direct[1]
            
            #in the range & curt_step(rooms[x][y] + 1) < rooms[x_][y_]
            if 0 <= x_ < len(rooms) and 0 <= y_ < len(rooms[0]) and rooms[x_][y_] > rooms[x][y] + 1:
                rooms[x_][y_] = rooms[x][y] + 1
                self.dfs(rooms, x_, y_)
  
  
  
  
  
  
  
  
  
  
  
典型bfs题目
  
code:
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return []
        
        queue = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue.append([i, j])
        
        while queue:
            room = queue.popleft()
            i = room[0]
            j = room[1]
            for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_i = i + direct[0]
                new_j = j + direct[1]
                if self.isvalid(rooms, new_i, new_j):
                    rooms[new_i][new_j] = rooms[i][j] + 1
                    queue.append([new_i, new_j])
            
        return rooms
    
    def isvalid(self, rooms, i, j):
        if 0 <= i < len(rooms) and 0 <= j < len(rooms[0]) and rooms[i][j] == 2**31 - 1:
            return True
        return False
