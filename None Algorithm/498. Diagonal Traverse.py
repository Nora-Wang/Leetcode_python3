Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.

# time: O(n * m), space: O(n * m)

# Utilize Flag to reverse
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix) or not len(matrix[0]):
            return []
        
        row = len(matrix)
        col = len(matrix[0])
        Flag = True
        res = []
        for x_y_sum in range(row + col - 1):
            x = 0 if x_y_sum <= col - 1 else x_y_sum - col + 1
            y = x_y_sum - x
            
            x_, y_ = x, y
            temp = []
            #print(x, y, x_y_sum)
            while 0 <= x_ < row and 0 <= y_ < col:
                temp.append(matrix[x_][y_])
                x_ += 1
                y_ -= 1
            
            if Flag:
                temp.reverse()
            #print(temp)
            res.extend(temp)
            Flag = not Flag
        
        return res
                
# 直接用sum的奇偶判断是否需要reverse
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix) or not len(matrix[0]):
            return []
        
        row = len(matrix)
        col = len(matrix[0])
        
        res = []
        for x_y_sum in range(row + col - 1):
            # 若为奇数，则从右上向左下
            if x_y_sum % 2:
                x = max(0, x_y_sum - col + 1)
                y = x_y_sum - x
                while 0 <= x < row and 0 <= y < col:
                    res.append(matrix[x][y])
                    x += 1
                    y -= 1
            # 若为偶数，则从左下向右上
            else:
                y = max(0, x_y_sum - row + 1)
                x = x_y_sum - y
                while 0 <= x < row and 0 <= y < col:
                    res.append(matrix[x][y])
                    x -= 1
                    y += 1
        
        return res
                
            
                
                        
