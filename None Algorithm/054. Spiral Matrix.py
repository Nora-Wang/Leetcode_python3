Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


 03/22/2020
 class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix) or not len(matrix[0]):
            return []
        
        n = len(matrix)
        m = len(matrix[0])
        visited = set([(0,0)])
        
        self.res = [matrix[0][0]]
        
        self.dfs(matrix, visited, 0, 0)
                    
        return self.res
                
    def dfs(self, matrix, visited, x_, y_):
        for direct in [(0,1),(1,0),(0,-1),(-1,0)] * (len(matrix) // 2 + 1):
            while 0 <= (x_ + direct[0]) < len(matrix) and 0 <= (y_ + direct[1]) < len(matrix[0]) and (x_ + direct[0], y_ + direct[1]) not in visited:
                x_ += direct[0]
                y_ += direct[1]
                
                visited.add((x_,y_))
                self.res.append(matrix[x_][y_])
                
        return
                
                
 
 
 
 
 
对matrix四个方向的pop

code:
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix) or not len(matrix[0]):
            return []
        
        result = []
        
        while matrix:
            #left to right pop
            #这里的pop(0)意思是对应matrix的第一行
            #这里用extend,节省空间
            result.extend(matrix.pop(0))
            
            #top to bottom pop
            if matrix and matrix[0]:
                #对matrix的每一行,pop出每一行的最后一个值
                for row in matrix:
                    result.append(row.pop())
            
            #right to left pop
            #对于matrix的最后一行进行pop,并将结果reverse
            if matrix:
                result.extend(matrix.pop()[::-1])
            
            #bottom to top pop
            if matrix and matrix[0]:
                #对于matrix的reversed每一行,pop出每一行的第一个值
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        
        return result
