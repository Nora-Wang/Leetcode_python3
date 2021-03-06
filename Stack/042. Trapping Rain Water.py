Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6


#06/08/2020
#brute force
#time: O(n^2), space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        res = 0
        
        for i in range(len(height)):
            left_max = max(height[:i + 1])
            right_max = max(height[i:])
            res += min(left_max, right_max) - height[i]
        
        return res
    
#DP prefix max    
每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度
从左到右扫描一边数组，获得每个位置往左这一段的最大值，再从右到左扫描一次获得每个位置向右的最大值。
然后最后再扫描一次数组，计算每个位置上的盛水数目。
#时间复杂度O(n)，空间复杂度O(n)

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

#同DP法，只是少写一个for loop + 少create一个O(n)的space 
#time: O(n), sapce: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        record = [0 for _ in range(len(height))]
        
        left_to_right = height[0]
        for i in range(len(height)):
            left_to_right = max(height[i], left_to_right)
            record[i] = left_to_right
        
        res = 0
        right_to_left = height[-1]
        for j in range(len(height) - 1, -1, -1):
            right_to_left = max(height[j], right_to_left)
            res += min(right_to_left, record[j]) - height[j]
        
        return res

    
#two pointer
#从两边向中间找两侧短板
#time: O(n), space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        
        max_left, max_right = height[0], height[-1]
        res = 0
        
        while left < right:
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                res += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])
        
        return res
    
