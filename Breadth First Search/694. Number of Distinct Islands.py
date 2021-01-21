Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:

11000
11000
00011
00011
Given the above grid map, return 1.
Example 2:

11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.
Note: The length of each dimension in the given grid does not exceed 50.


BFS,需要判断形状,因此记录点的相对位置来判断形状是否相同

code:
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        
        #将每个island的形状记录一下,用set避免重复
        graphs = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                graph = self.get_graphs(grid, i, j)
                # 这里graph是用的list做的，而set中不能存list，因此转化成tuple类型
                graphs.add(tuple(graph))
        
        return len(graphs)
    
    def get_graphs(self, grid, i, j):
        queue = collections.deque([(i,j)])
        
        grid[i][j] = 0
        
        #这里的graph先用list存，等最后得到一个结果后，在转成tuple类型
        graph = []
        
        while queue:
            x,y = queue.popleft()
            
            for direct in DIRECTIONS:
                x_ = x + direct[0]
                y_ = y + direct[1]
                
                if self.is_valid(grid, x_, y_):
                    queue.append((x_,y_))
                    grid[x_][y_] = 0
                    graph.append((x_ - i, y_ - j))
        
        return graph
        
    
    def is_valid(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        
        if grid[x][y] == 0:
            return False
        
        return True
