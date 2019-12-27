Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
  
思路:
假设矩阵A，B均为 n x n 的矩阵，
矩阵A的稀疏系数为a，矩阵B的稀疏系数为b，
a，b∈[0, 1]，矩阵越稀疏，系数越小。
  
  
code:
Version 1
暴力，不考虑稀疏性
Time (n^2 * (1 + n)) = O(n^2 + n^3)
Space O(1)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(A) or not len(A[0]) or not len(B):
            return []
        
        A_r = len(A)
        A_c = len(A[0])
        B_c = len(B[0])
        
        #initial result
        result = [0] * A_r
        for i in range(len(result)):
            result[i] = [0] * B_c
                
        for i in range(A_r):
            for j in range(B_c):
                for k in range(A_c):
                    result[i][j] += A[i][k] * B[k][j]
        
        return result
      
      
Version 2
改进,考虑A的稀疏性,在二重for循环的时候将A为0的情况continue掉,以减少三重循环的次数
Time O(n^2 * (1 + a * n) = O(n^2 + a * n^3)
Space O(1)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(A) or not len(A[0]) or not len(B):
            return []
        
        A_r = len(A)
        A_c = len(A[0])
        B_c = len(B[0])
        
        #initial result
        result = [0] * A_r
        for i in range(len(result)):
            result[i] = [0] * B_c
                
        for i in range(A_r):
            for k in range(A_c):
                if A[i][k] == 0:
                    continue
                for j in range(B_c):
                    result[i][j] += A[i][k] * B[k][j]
        
        return result
      
      
Version 3
进一步改进，考虑A与B的稀疏性,将B预处理,记录B的一行中非0元素的列数,在第三重循环的时候直接调用非0元素即可
Time O(n^2 * (1 + a * b * n)) = O(n^2 + a * b * n^3)
Space O(b * n^2)
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        if not len(A) or not len(A[0]) or not len(B):
            return []
        
        A_r = len(A)
        A_c = len(A[0])
        B_c = len(B[0])
        
        #initial result
        result = [0] * A_r
        for i in range(len(result)):
            result[i] = [0] * B_c
            
        #preprocessing B
        B_pre = []
        for i in range(A_c):
            temp = []
            for j in range(B_c):
                if B[i][j] != 0:
                    temp.append(j)
            B_pre.append(temp)
                
        for i in range(A_r):
            for k in range(A_c):
                if A[i][k] == 0:
                    continue
                for j in B_pre[k]:
                    result[i][j] += A[i][k] * B[k][j]
        
        return result
