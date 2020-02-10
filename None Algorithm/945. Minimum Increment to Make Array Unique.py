Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.

 

Example 1:

Input: [1,2,2]
Output: 1
Explanation:  After 1 move, the array could be [1, 2, 3].
Example 2:

Input: [3,2,1,2,1,7]
Output: 6
Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
 

Note:

0 <= A.length <= 40000
0 <= A[i] < 40000


code:
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        
        count = 0
        #排个序
        A.sort()
        
        for i in range(1,len(A)):
            #当后面的值比前一个大,即表示该值不用move
            if A[i] > A[i-1]:
                continue
            
            #记录当前值
            temp = A[i]
            
            #将当前值变为前一个值+1,因为整个list是sorted过的,因此一定是递增的
            A[i] = A[i-1] + 1
            
            #得到当前值需要move多少
            count += A[i] - temp
        
        return count
            
            
            
            
        
