题目：
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


思路：
方法1:先按每行的首个数字二分确定target所在的行，再在该行中二分搜索target
方法2:将整个二维数组转换为一个一维数组，再进行二分搜索target
方法3:看成一维数组，二分查找，其中看成一维数组的序号id和二维数组中行号、列号对应关系为：row_num = id/m;  col_num = id%m;

code:
#方法1
#T(n) = O(log(n) + log(m)) = O(log(n*m))
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return False
        m = len(matrix[0])
        n = len(matrix)

        #the first position
        start = 0
        end = n - 1
        row_num = 0
        while(start + 1 < end):
            mid = start + (end - start) / 2
            if(matrix[mid][0] == target):
                return True
            if(matrix[mid][0] < target):
                start = mid
            else:
                end = mid
        if(matrix[end][0] <= target):
            row_num = end
        elif(matrix[start][0] <= target):
            row_num = start
        else:
            return False
            
        #the second position
        start = 0
        end = m - 1
        while(start + 1 < end):
            mid = start + (end - start) / 2
            if(matrix[row_num][mid] == target):
                return True
            if(matrix[row_num][mid] < target):
                start = mid
            else:
                end = mid
        if(matrix[row_num][start] == target):
            return True
        if(matrix[row_num][end] == target):
            return True
        return False
        
        
#方法2                
#T(n) = n + log(n * m)
       class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if(len(matrix) == 0 or len(matrix[0]) == 0):
            return False
        m = len(matrix[0])
        n = len(matrix)
        i = 0
        list = []
        while(i < n):
            list += matrix[i]
            i += 1
        start = 0
        end = len(list) - 1
        while(start + 1 < end):
            mid = start + (end - start) / 2
            if(list[mid] == target):
                return True
            if(list[mid] < target):
                start = mid
            else:
                end = mid
        if(list[start] == target):
            return True
        if(list[end] == target):
            return True
        return False
                
        
        
         
        
        
