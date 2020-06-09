Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10


#brute force
#对每一个height做背向双指针
#time: O(n^2), space: O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        res = 0
        for i in range(len(heights)):
            left, right = i - 1, i + 1
            count = 1
            
            while left >= 0 and heights[left] >= heights[i]:
                count += 1
                left -= 1
                
            while right < len(heights) and heights[right] >= heights[i]:
                count += 1
                right += 1
            
            res = max(res, count * heights[i])
        
        return res
       
       

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #注意第一位加个0,这样才能保证后续的stack[-1]不会超出范围
        #注意最后一位加个0,才能保证stack里所有的点都被弹出,每个高度的面积都被算过
        heights = [0] + heights + [0]
        stack, max_rec = [], 0
        
        #从左向右遍历
        for right_index, height in enumerate(heights):
            #当遇到第一个小于前面的高度的位置，开始计算所有大于该高度的面积 
            while stack and height < heights[stack[-1]]:
                #每次弹出一个，计算弹出高度距当前index的面积 
                #比如遇到2以后，先计算6的，再计算56的 
                popped_index = stack.pop()
                
                #左侧的index是弹出后栈顶的index
                left_index = stack[-1]
                
                #计算弹出位置的宽度
                width = right_index - left_index - 1
                
                ##保留最大面积值
                max_rec = max(max_rec, width * heights[popped_index])
            
            #压入当前index
            stack.append(right_index)
        
        return max_rec
                
                
        
        
