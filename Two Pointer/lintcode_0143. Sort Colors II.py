Given an array of n objects with k different colors (numbered from 1 to k), sort them so that objects of the same color are adjacent, with the colors in the order 1, 2, ... k.

Example

Example1

Input: 
[3,2,2,1,4] 
4
Output: 
[1,2,2,3,4]
Example2

Input: 
[2,1,1,2,2] 
2
Output: 
[1,1,2,2,2]
Challenge

A rather straight forward solution is a two-pass algorithm using counting sort. That will cost O(k) extra memory. Can you do it without using extra memory?

Notice

You are not suppose to use the library's sort function for this problem.
k <= n


思路:
用快排,使用分治法来解决
参考lintcode_0031. Partition Array

具体步骤：
传入两个区间,一个是颜色区间color_start, color_end;另外一个是待排序的数组区间 index_start, index_end
找到颜色区间的中点pivot,将数组范围内进行partition; <= pivot 的去左边，> pivot 的去右边;然后继续递归

时间复杂度O(nlogk),n是数的个数,k是颜色数目。这是基于比较的算法的最优时间复杂度。
不基于比较的话，可以用计数排序（Counting Sort）

code:
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        if not colors:
            return []
            
        self.sort(colors, 1, k, 0, len(colors) - 1)
        
    def sort(self, colors, colors_start, colors_end, index_start, index_end):
        #注意这里是or
        if colors_start >= colors_end or index_start >= index_end:
            return
        
        #注意这里的pivot是取得k different colors的中间值
        #不是colors这个array的中间值:pivot = colors[index_start + (index_end - index_start) // 2]
        pivot = colors_start + (colors_end - colors_start) // 2
        #快排模板,注意这里要另设一个left和right
        left, right = index_start, index_end
        
        while left <= right:
            #这里将colors[left] == pivot的情况放在了左侧
            #因为pivot = (color_start + color_end) // 2 是向下取整的 所以等于的在左边,和pivot同侧
            while left <= right and colors[left] <= pivot:
                left += 1
            while left <= right and colors[right] > pivot:
                right -= 1
                
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1
                
        #注意这里divide and conquer时函数的取值范围.具体理解可参考sort algorithm中quick sort的解释
        self.sort(colors, colors_start, pivot, index_start, right)
        self.sort(colors, pivot + 1, colors_end, left, index_end)
