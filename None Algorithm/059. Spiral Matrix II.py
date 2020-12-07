Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

# 12/07/2020
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        num = 1
        start_index = 0
        
        while n > 0:
            num = self.fill_matrix(matrix, n, num, start_index)
            n -= 2
            start_index += 1
        
        return matrix
    
    def fill_matrix(self, matrix, n, num, start_index):
        # left -> right
        for j in range(n):
            matrix[start_index][start_index + j] = num
            num += 1
        
        # top -> down
        for i in range(1, n):
            matrix[start_index + i][start_index + n - 1] = num
            num += 1
        
        # right -> left
        for j in range(n - 2, -1, -1):
            matrix[start_index + n - 1][start_index + j] = num
            num += 1
        
        # down -> top
        for i in range(n - 2, 0, -1):
            matrix[start_index + i][start_index] = num
            num += 1
        
        return num
        


# 03/22/2020
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        self.res = [[None for _ in range(n)] for _ in range(n)]
        
        self.dfs(n, 0, 0, set(), 1)
        
        return self.res
    
    def dfs(self, n, x, y, visited, value):
        for direct in [(0,1),(1,0),(0,-1),(-1,0)] * n:
            visited.add((x,y))
            self.res[x][y] = value
            
            while 0 <= (x + direct[0]) < n and 0 <= (y + direct[1]) < n and (x + direct[0], y + direct[1]) not in visited:
                x += direct[0]
                y += direct[1]
                
                value += 1
                visited.add((x,y))
                self.res[x][y] = value
            
            if value == (n * n + 1):
                return





四个方向跑一遍,即将最外层赋值,然后循环进入下一层即可


code:
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[None for _ in range(n)] for _ in range(n)]
        
        row, col = 0, 0
        num = 0
        
        #这里直接<即可,因为后续是先+,再放入值;在最后直接放的就是n*n
        #注意对四角的处理,可能会重复
        while num < n * n:
            #left -> right(curt row = row)
            if row < n:
                for j in range(col, n - col):
                    num += 1
                    res[row][j] = num
            
            #up -> down(last col = n - col - 1)
            if row < n and col < n:
                for i in range(row + 1, n - row):
                    num += 1
                    res[i][n - col - 1] = num
            
            #right -> left(last row = n - row - 1)
            if row < n:
                for j in range(n - col - 2, col, -1):
                    num += 1
                    res[n - row - 1][j] = num
            
            #down -> up(first col = col)
            if row < n and col < n:
                for i in range(n - row - 1, row, -1):
                    num += 1
                    res[i][col] = num
            
            #下一层
            row += 1
            col += 1
        
        return res
            
            
            
            
