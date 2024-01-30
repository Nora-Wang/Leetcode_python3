You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

# 1/30/2024
# More clear logistic for one loop with O(1) space
# https://leetcode.com/problems/rotate-image/discuss/367514/python-beats-96-with-Image-helps-u-understand
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not len(matrix) or not len(matrix[0]):
            return
        
        self.n = len(matrix)
        if self.n <= 1:
            return
        
        for i in range((self.n + 1) // 2):
            # j就是从第i层开始的第一列到第i层结束的最后一列
            for j in range(i, self.n - i - 1):
                i_r, j_r = self.rotate_pos_clockwise(i, j)
                i_b, j_b = self.rotate_pos_clockwise(i_r, j_r)
                i_l, j_l = self.rotate_pos_clockwise(i_b, j_b)
                
                up = matrix[i][j]
                matrix[i][j] = matrix[i_l][j_l]
                matrix[i_l][j_l] = matrix[i_b][j_b]
                matrix[i_b][j_b] = matrix[i_r][j_r]
                matrix[i_r][j_r] = up
        return

    # 一行一共是n-i*2个node
    # 1. 上下翻 i,j -> n-i-1,j
    # 2. 对角翻 n-i-1,j -> j,n-i-1
    def rotate_pos_clockwise(self, i, j):
        return j, self.n - 1 - i


# 1/18/21
# optimal: one loop with O(1) space
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 一共有n // 2层需要旋转
        for i in range(n // 2):
            # 每一层分为4个部分
            # j代表这一层需要旋转的个数
            for j in range(i, n - i - 1):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
                matrix[j][n - 1 - i] = temp
        
        return
            



题目中说了不能另开matrix,因此只能在原有matrix基础上改变
两步翻转:
1.上下翻转
2.对角线翻转


code:
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not len(matrix) or not len(matrix[0]):
            return []
        
        n = len(matrix)
        
        #上下翻转
        for i in range(n // 2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        
        #对角线翻转
        for i in range(n):
            for j in range(i,n):
                if i == j:
                    continue
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
