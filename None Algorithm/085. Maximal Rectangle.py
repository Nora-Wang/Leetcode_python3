Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6


code:
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0
        
        #初始化高度列表，把矩阵转化成Rectangle in Histogram
        heights = [0] * len(matrix[0])
        result = 0
        
        #遍历每一行
        for row in matrix:
            #穷举当前行得元素，制作高度列表
            for index, value in enumerate(row):
                #如果当前高度有值'1',把之前的高度列表的高度加1;如果没有值,重置高度列表为0,相当于与之前的完全断开
                if value == '1':
                    heights[index] += 1
                else:
                    heights[index] = 0
            
            #计算当前层最大的面积
            row_max = self.get_maximal_rectangle(heights)
            result = max(result, row_max)
        
        return result
    
    #这部分直接参考leetcode84题,一模一样
    def get_maximal_rectangle(self, heights):
        heights = [0] + heights + [0]
        stack, max_rec = [], 0
        
        for r_index, height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                popped_index = stack.pop()
                
                l_index = stack[-1]
                
                width = r_index - l_index - 1
                
                max_rec = max(max_rec, width * heights[popped_index])
            
            stack.append(r_index)
        
        return max_rec
