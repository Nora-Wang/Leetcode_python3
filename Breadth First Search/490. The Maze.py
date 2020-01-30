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


主要思路：
简短复述一下题意：
给定一个由 0 1 构成的迷宫(maze)，再给定一个起始坐标start和一个目的地坐标destination。
从start出发，可以向上下左右四个方向移动，碰到墙壁才会停止，然后才可以转向。
另外，只有停在destination的位置上才行，经过不算。
返回true或者false。


注意：
1.关于搜索中去重，主要保证不会停在同一个地方重复搜索即可
这里用visited记录每次停下时的坐标，即每次pop出一个新point坐标时，检查当前位置是否在visited中；若不在，加入visited
2.若point是挨着墙的，如point的右侧为墙，则其无法进行valid_roll，最后返回的new=stop_point，若此时再将该点append进queue，相当于重复工作，
时间复杂度会大大增加；因此在将new放入queue前，需要判断其是否与stop_point(即起始点)相同，若不同，再加入queue


BFS：停下若不在原点则入队，出队检查去重
每次pop新坐标之后先检查是否在visited中，如果不在，加入visited中，然后向四个方向搜索，走到撞墙，把判断完valid+不与原点相同的坐标加入queue；
  

code:
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        if not len(maze) or not len(maze[0]):
            return False
        
        if start == destination:
            return True
        
        queue = collections.deque([(start)])
        visited = set([(start[0],start[1])])

        
        while queue:
            x,y = queue.popleft()

            for direct in DIRECTIONS:
                x_, y_ = x, y
    
                while self.is_valid(maze, x_ + direct[0], y_ + direct[1]):
                    x_ += direct[0]
                    y_ += direct[1]
                
                if (x_,y_) in visited:
                    continue
                
                if [x_,y_] == destination:
                    return True
                
                visited.add((x_,y_))
                queue.append([x_,y_])
        
        return False
                
    
    def is_valid(self, maze, x, y):
        if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
            return False
        
        if maze[x][y] == 1:
            return False
        
        return True
                


        
