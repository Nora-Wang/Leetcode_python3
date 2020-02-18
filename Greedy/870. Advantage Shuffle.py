Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: A = [12,24,8,32], B = [13,25,32,11]
Output: [24,32,8,12]
 

Note:

1 <= A.length = B.length <= 10000
0 <= A[i] <= 10^9
0 <= B[i] <= 10^9


Greedy + Two pointer
将B所有的值都以tuple的形式(value, index)放入一个list,并且以value为标准进行从小到大的排序,A也排序;
然后用two pointer,若当前A的值比B的大,则正常将A的值A[A_start]放入B值对应的index中;
若当前A的值比B的小,则将A最后的值A[A_end]放入B值对应的index中

code:
import heapq
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        res = [-1 for num in A]
        
        #Use tuple which is convenient for later to use index
        B_tuple = []
        for i in range(len(B)):
            B_tuple.append((B[i],i))
        
        #sort A and B
        A.sort(reverse=True)
        B_tuple.sort(reverse=True)
        
        #Two Pointer
        A_start = 0
        A_end = len(A) - 1
        for b,index in B_tuple:
            if b < A[A_start]:
                res[index] = A[A_start]
                A_start += 1
            else:
                #这里直接将A最后的值倒着放入对应的index,是因为在前面的if循环结束,最后的A值会剩下,然后被依序放入res
                res[index] = A[A_end]
                A_end -= 1
        
        return res
        
