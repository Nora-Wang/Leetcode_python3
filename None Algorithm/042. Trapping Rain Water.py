Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度

从左到右扫描一边数组，获得每个位置往左这一段的最大值，再从右到左扫描一次获得每个位置向右的最大值。
然后最后再扫描一次数组，计算每个位置上的盛水数目。

时间复杂度O(n)，空间复杂度O(n)

code:
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left_max = [None] * len(height)
        left_record = 0
        for i in range(len(height)):
            left_max[i] = max(left_record, height[i])
            left_record = left_max[i]
        
        right_max = [None] * len(height)
        right_record = 0
        for i in range(len(height) - 1, -1, -1):
            right_max[i] = max(right_record, height[i])
            right_record = right_max[i]
        
        result = 0
        for i in range(len(height)):
            result += min(left_max[i], right_max[i]) - height[i]
        
        return result
