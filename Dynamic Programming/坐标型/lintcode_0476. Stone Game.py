There is a stone game.At the beginning of the game the player picks n piles of stones in a line.

The goal is to merge the stones in one pile observing the following rules:

At each step of the game,the player can merge two adjacent piles to a new pile.
The score is the number of stones in the new pile.
You are to determine the minimum of the total score.

Example

Example 1:

Input: [3, 4, 3]
Output: 17
Example 2:

Input: [4, 1, 1, 4]
Output: 18
Explanation:
  1. Merge second and third piles => [4, 2, 4], score = 2
  2. Merge the first two piles => [6, 4]，score = 8
  3. Merge the last two piles => [10], score = 18
  
  

code:
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        return self.helper(A, 0, len(A) - 1, {})
        
    def helper(self, A, start, end, memo):
        if (start, end) in memo:
            return memo[(start, end)]
            
        #如果遍历完了，就返回0 （A为[]时，len(A) - 1为-1，start > end）
        if start >= end:
            return 0
            
        #当前层的花费为A中start和end中所有值的和   
        cost = sum(A[start:end + 1])
        min_cost = sys.maxsize
        
         #切分A的每一部分进行遍历
        for mid in range(start, end):
            #分别计算切分的左边的值和右边的值
            left = self.helper(A, start, mid, memo)
            #如果mid==end，mid+1会超范围
            right = self.helper(A, mid + 1, end, memo)
            #记录最小值
            min_cost = min(min_cost, left + right + cost)
            
        memo[(start, end)] = min_cost
        return min_cost
