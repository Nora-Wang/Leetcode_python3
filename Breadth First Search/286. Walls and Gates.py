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
