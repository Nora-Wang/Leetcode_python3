题目：
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


# 09/08/2020
# method 1
'''
do twice binary search
1. do binary search based on the first col -> find out while row the target shoud be
2. do binary search based on the curtain matrix row -> find out the target
time: O(logn + logm) = O(log(n*m)), space: O(1), n = len(matrix), m = len(matrix[0])
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]) or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        row = self.find_row(matrix, target)
        col = self.find_col(matrix[row], target)
        
        return col != -1
    
    def find_row(self, matrix, target):
        start, end = 0, len(matrix) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            
            if matrix[mid][0] == target:
                return mid
            
            if matrix[mid][0] < target:
                start = mid
            else:
                end = mid
        
        # 判断target是否在matrix[start]这一行的范围里
        if matrix[start][0] <= target <= matrix[start][-1]:
            return start
        return end
    
    def find_col(self, nums, target):
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

# method 2
'''
method 2:
do onice binary search
left = 1, right = n * m
m = number of cols -> 除法得到该在第几行，取余得到该在第几列
row = mid // m
col = min % m
time: O(log(n*m)) = O(log(n) + log(m)), space: O(1)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not len(matrix) or not len(matrix[0]) or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        n, m = len(matrix), len(matrix[0])
        
        start, end = 0, n * m - 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] < target:
                start = mid
            else:
                end = mid
        
        return matrix[start // m][start % m] == target or matrix[end // m][end % m] == target


    
    

思路：
方法1:先按每行的首个数字二分确定target所在的行，再在该行中二分搜索target
方法2:将整个二维数组转换为一个一维数组，再进行二分搜索target
方法3:看成一维数组，二分查找，其中看成一维数组的序号id和二维数组中行号、列号对应关系为：row_num = id/m;  col_num = id%m;

code:
#方法1
#T(n) = O(log(n) + log(m)) = O(log(n*m)) = O(log(n))
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
#T(n) = O(n + log(n * m)) = O(n + log(n)) = O(n)
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
  #######第二次用这个方法的时候，写的是
    ######list.append(matrix[i])
    ######这样写不行！！因为matrix[0]的结果为[[1,2,3,4]]
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
                
        
        
         
        
        
