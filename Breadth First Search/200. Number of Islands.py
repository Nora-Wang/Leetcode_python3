题目：
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1


思路：用count记录island的个数，当一个node的值为1，用bfs遍历其上下左右四个点，若为1，则赋值为0
count = 0
for node = 1 in grid:
    self.bfs(node)
    count += 1
return count

注意点：
bfs的时候需要判断一下这个node是否在矩阵范围内，且node的值为1 def node_valiable(self, grid, x, y)
坐标变换数组：对于grid[i][j]的上下左右node，用set类型的dir与x,y加减得到 dir = ([-1,0],[1,0],[0,-1],[0,1])

code:
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        
        count = 0
        len_r = len(grid)
        len_c = len(grid[0])
        for i in range(len_r):
            for j in range(len_c):
                if grid[i][j] == '1':
                    self.bfs(grid, i, j)
                    count += 1
        return count
    
    def bfs(self, grid, x, y):
        dir = ([-1,0],[1,0],[0,-1],[0,1])
        queue = collections.deque([(x, y)])
        grid[x][y] = '0'
        while queue:
            x, y = queue.popleft()
            for [move_x,move_y] in dir:
                next_x = x + move_x
                next_y = y + move_y
                if self.node_valiable(grid, next_x, next_y):
                    grid[next_x][next_y] = '0'
                    queue.append((next_x, next_y))

    
    def node_valiable(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1'
            
