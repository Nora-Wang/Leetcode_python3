In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.


code:
DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return -1
        
        queue = collections.deque([])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
        count = 0
        
        while queue:
            for _ in range(len(queue)):
                x,y = queue.popleft()
                for direct in DIRECTIONS:
                    x_ = x + direct[0]
                    y_ = y + direct[1]
                    
                    if self.is_valid(x_, y_, grid):
                        grid[x_][y_] = 2
                        queue.append((x_,y_))
            count += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        #这里要注意corner case
        #当grid里只有0时,count为0
        if count == 0:
            return 0
        #这里要-1是因为一般如果把count放在for循环后面,是计算edge个数,其是node个数-1,但这种是在for循环里面就直接return,
        #即不会执行最后一次for循环的count+1;但这里不是,因此需要在最后结果-1
        return count - 1
    
    def is_valid(self, x, y, grid):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
            return False
        
        if grid[x][y] == 2:
            return False
        
        if grid[x][y] == 0:
            return False
        
        return True
            
