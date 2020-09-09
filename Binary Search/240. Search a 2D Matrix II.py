题目：
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


# 09/09/2020
'''
n = number of col, m = number of row

M1: brute force
traverse all the elements in matrix
time: O(n * m), space: O(1)

M2: binary search for every row/every col, depends on n and m
time: O(min(mlogn. nlogm)), space: O(1)

M3: utilize the conditions to solve
以右上角为标准，因为条件给了，每一行中最右侧最大，每一列中最上面的最小，因此当发现当前num < target，则往下走;当发现当前num > target，则往左走
time: O(n + m), space: O(1)
'''
# M3 code
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]) or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        
        while row < m and col >= 0:
            curt = matrix[row][col]
            
            if curt == target:
                return True
            
            if curt < target:
                row += 1
            else:
                col -= 1
        
        return False




思路：
矩阵特点：每一行和每一列递增

从左下角往右上角找，有如下三种情况：

元素 = target，返回true
元素 < target，下一步向右走，因为右边的元素都大于当前元素，上方元素小于当前元素
元素 > target，下一步向上走，因为右边的元素都大于当前元素，上方元素小于当前元素

####第二次做的时候知道应该从左下往右上走，但因为对题目的理解不深，不知道为什么可以如此判断。以下两句话要仔细理解！！
####Integers in each row are sorted in ascending from left to right.
####Integers in each column are sorted in ascending from top to bottom.

code:

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #n和m分开判断：若matrix=[]，则不存在matrix[0]（m = len(matrix[0])）
        n = len(matrix)
        if(n <= 0):
            return False
        m = len(matrix[0])
        if(m <= 0):
            return False
        row = n - 1
        col = 0
        while(row >= 0 and col < m):
            if(matrix[row][col] == target):
                return True
            if(matrix[row][col] > target):
                row = row - 1
            else:
                col = col + 1
        return False
                
        
        
