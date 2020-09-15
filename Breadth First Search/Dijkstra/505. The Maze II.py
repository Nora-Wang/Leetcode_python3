There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

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

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

# 方法 1:
'''
Dijkstra + hashset
用一个visited_set存储已经判断过的点
'''
from heapq import heappush, heappop
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if start == destination:
            return True
        
        heap = []
        heappush(heap, (0, start[0],start[1]))
        # initialize visited 的时候不加入start: 因为visited需要被放在heappop处，而不是heappush处
        visited = set()
        
        while heap:
            step, x, y = heappop(heap)
            
            # 判断是否 == destination需要放在heappop处
            # 因为如果放在后面，即用x_,y_来判断，则可能出现一个情况：同一个loop的一个点先滚到destination，但其distance其实比同loop的一个点大，导致最后结果不是shortest distance
            if [x,y] == destination:
                return step
            
            # visited需要放在heappop处
            # 原因跟上面判断destination差不多，担心其中一个点先到达一个点，但其实另一个点到该点到距离更短
            if (x,y) in visited:
                continue
            visited.add((x,y))
            
            for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
                x_, y_ = x, y
                count = 0
                
                while self.valid(maze, x_ + direct[0], y_ + direct[1]):
                    x_ += direct[0]
                    y_ += direct[1]
                    count += 1
                
                heappush(heap, (step + count, x_, y_))
                    
        
        return -1
    
    def valid(self, maze, x, y):
        if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
            return False
        
        if maze[x][y] == 1:
            return False
        
        return True


# 方法 2:
'''
Dijkstra + 二维数组
用一个二维数组存取start到每个点到distance + BFS
'''
import heapq
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        if not len(maze) or not len(maze[0]):
            return False
        
        if start == destination:
            return True
        
        #初始化二维数组
        #二维数组一定要设置,用于判断是否比之前的path小,若小,则继续向下走
        distance = [[sys.maxsize for i in range(len(maze[0]))] for j in range(len(maze))]
        distance[start[0]][start[1]] = 0
        
        #将start放入heap,heap中存入当前点到start的距离,当前点的坐标
        heap = []
        heapq.heappush(heap, (0, start[0],start[1]))
        
        while heap:
            #prev代表当前点到start的距离
            prev, x, y = heapq.heappop(heap)
            
            #若为destination则直接输出即可,因为所得到的prev一定是start到destination的最短距离
            if [x,y] == destination:
                return prev
            
            for direct in DIRECTIONS:
                x_,y_ = x,y
                #将count复制为prev,这样获得当前点到start的距离+后续其roll的距离,就是下一个点到start的距离;因此heap直接将count记录即可
                count = prev
                
                while self.is_valid(maze, x_ + direct[0], y_ + direct[1]):
                    x_ += direct[0]
                    y_ += direct[1]
                    count += 1
                
                if count < distance[x_][y_]:
                    distance[x_][y_] = count
                    heapq.heappush(heap, (count, x_,y_))

        return -1
    
    def is_valid(self, maze, x, y):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 0
        
 
 
 
#BFS:queue+二维数组 Version
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not len(maze) or not len(maze[0]):
            return -1
        
        #corner case
        if start == destination:
            return 0
        
        queue = collections.deque([(start)])
        #用一个二维数组distance记录maze中的每个点到start的距离
        distance = [[sys.maxsize for i in range(len(maze[0]))] for j in range(len(maze))]
        distance[start[0]][start[1]] = 0
        
        while queue:
            x,y = queue.popleft()
            #四个方向
            for direct in DIRECTIONS:
                count = distance[x][y]
                x_, y_ = x, y
                
                #注意这里的写法,因为想要最后得到的x_,y_为停下的点,而不是墙/超出范围,因此在判断是否valid的时候是用的x_ + direct[0], y_ + direct[1]
                while self.is_valid(maze, x_ + direct[0], y_ + direct[1]):
                    x_ += direct[0]
                    y_ += direct[1]
                    count += 1
                
                #这里要取最小值,因为判断这一次起点到该点是不是最短路程,如果是再加入队列中,更新该点值 
                #如果是第一次到该点，则一定小于极大值
                if count < distance[x_][y_]:
                    distance[x_][y_] = count
                    queue.append((x_,y_))

        #如果终点的distance为sys.maxsize,则说明从起点无法到达终点,因此返回-1
        if distance[destination[0]][destination[1]] == sys.maxsize:
            return -1
        return distance[destination[0]][destination[1]]
                
    
    def is_valid(self, maze, x, y):
        if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
            return False
        
        if maze[x][y] == 1:
            return False
        
        return True
                


