Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Example

Example 1:

Input:[2,7,11,15]
Output:[]
Example 2:

Input:[-1,0,1,2,-1,-4]
Output:	[[-1, 0, 1],[-1, -1, 2]]
Notice

Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.


1.暴力枚举三个数复杂度为O(N^3),即for循环a * for循环b * for循环c

2.使用Two Sum的做法
总体思路：在sorted array中枚举a，因为题目要求得到a + b + c = 0的结果，因此可以将-a设为target，即-a = b + c
然后用two sum的two pointer的方法，在限定范围内找到b和c的组合值，以此解决问题

使用有序数列的好处是，在枚举和移动指针时值相等的数可以跳过，省去去重部分

注意：对于two pointer的array的取值范围，应该是a之后的范围？？？？

具体步骤：
假设升序数列a，对于一组解ai,aj, 另一组解ak,al,其必然满足 i<k + j>l 或 i>k + j<l
因此我们可以用two pointer，初始时指向数列两端,指向数之和大于目标值时，右指针向左移使得总和减小，反之左指针向右移

时间复杂度：
由此可以用O(N)的复杂度解决Two Sum问题，再加上枚举a的复杂度为O(N),前面虽然用了sort，但其复杂度为O(nlogn)<O(n^2),因此整个3Sum的复杂度为O(N^2)




code:
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if not numbers:
            return []
            
        numbers.sort()
        size = len(numbers)
        self.results = []
        
        #由于有3个值，因此a的取值范围仅能到size - 2
        for i in range(size - 2):
            #去重：对a的值去重
            if i and numbers[i] == numbers[i - 1]:
                continue
            #注意这里的start = i + 1,此时的numbers[i]即a,即find_two_sum中numbers的取值范围是a～最后一个值
            #这是因为two sum是要在a的右侧找到b和c
            self.find_two_sum(numbers, i + 1, size - 1, -numbers[i])
        
        return self.results
        
    #这部分同587. Two Sum - Unique pairs的Version 2
    def find_two_sum(self, numbers, start, end, target):
        while start < end:
            if numbers[start] + numbers[end] == target:
                #注意这里的返回值，由小到大排序
                self.results.append([-target, numbers[start], numbers[end]])
                start += 1
                end -= 1
                #去重
                while start < end and numbers[start] == numbers[start - 1]:
                    start += 1
                while start < end and numbers[end] == numbers[end + 1]:
                    end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
                
