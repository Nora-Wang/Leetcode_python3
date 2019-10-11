There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.



code:
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        visited = []
        dic_r = [0,0,1,-1]
        dic_c = [1,-1,0,0]
        queue = collections.deque([start])
        while queue:
            stop_point = queue.popleft()
            row = stop_point[0]
            col = stop_point[1]
            if [row, col] in visited:
                continue
            else:
                visited.append([row, col])
            for i in range(0, 4):
                new = [row, col]
                while self.valid_roll((new[0] + dic_r[i], new[1] + dic_c[i]), maze):
                    new[0] += dic_r[i]
                    new[1] += dic_c[i]
                if new == destination:
                    return True
                queue.append([new])
        return False
    
    def valid_roll(self, new_node, maze):
        row = new_node[0]
        col = new_node[1]
        if row < 0 or row >= len(maze) or col < 0 or col >= len(maze[0]):
            return False
        if maze[row][col] == 1:
            return False
        return True
        
