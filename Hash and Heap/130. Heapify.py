Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].
Example

Example 1

Input : [3,2,1,4,5]
Output : [1,2,3,4,5]
Explanation : return any one of the legitimate heap arrays
Challenge

O(n) time complexity

Clarification

What is heap? What is heapify? What if there is a lot of solutions?

Heap is a data structure, which usually have three methods: push, pop and top. where "push" add a new element the heap, "pop" delete the minimum/maximum element in the heap, "top" return the minimum/maximum element.
Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i], we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].
Return any of them.


code:
class Solution:
    """
    @param: A: Given an integer array
    @return: nothing
    """
    def heapify(self, A):
        if not A:
            return []
            
        index = []
        #因为堆的后半部分一定不用向下换,所以直接从1/2开始,倒序来找
        for i in range(len(A) // 2, -1, -1):
            self.switch_down(A, i)
        
        return A
        
    def switch_down(self, A, curt):
        #当当前点左孩子小于总长度时(当前点可向下换),进行判断
        while curt * 2 + 1 < len(A):
            #算出左右孩子的下标
            son = curt * 2 + 1
            #在右孩子存在的,有效的前提下(因为右孩子可能超范围)
            #如果左孩子的值大于右孩子的值,把son更新为右孩子的下标
            right_son = curt * 2 + 2
            if right_son < len(A) and A[son] > A[right_son]:
                son = right_son
            
            #如果son的值大于当前点值,此时左右孩子的值都大于当前点,不用换
            if A[curt] <= A[son]:
                break
            
            #如果小于当前点的值,交换当前点和son的值
            A[curt], A[son] = A[son], A[curt]
            #更新当前点的下标为son,继续判断是否能继续往下换
            curt = son
            
            
