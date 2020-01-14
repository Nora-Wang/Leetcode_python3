Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall. How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.

Example

Example 1:

Input:
[[0,1,2,0,0],
 [1,0,0,2,1],
 [0,1,0,0,0]]
Output:
2
Example 2:

Input:
[[0,0,0],
 [0,0,0],
 [0,0,1]]
Output:
4


code:
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        if not grid or not grid[0]:
            return 0
        
        queue = collections.deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append([i, j])
        
        count = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                for direct in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_i = node[0] + direct[0]
                    new_j = node[1] + direct[1]
                    if self.is_valid(grid, new_i, new_j):
                        grid[new_i][new_j] = 1
                        queue.append([new_i, new_j])
            count += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    return -1
        #重要知识点!!!!
        #因为while queue的时候,当queue = deque([])时,也会进行一次循环,这样就导致count会多加一次
        #与course schedule作对比会发现,之所以course schedule不用减一是因为count从0开始设置的,即第一门课没有被算上,
        #本来while循环结束count应该 = len(course) - 1,但因为多一次循环,因此count = len(course)
        return count - 1
    
    def is_valid(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False
            
        if grid[i][j] == 2 or grid[i][j] == 1:
            return False
        
        return True
