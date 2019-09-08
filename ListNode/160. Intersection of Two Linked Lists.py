题目：
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.




思路：
主要思路很简单：pa和pb都将headA和headB遍历一遍（pa有值则.next,为空则换成headB），最后一定会在intersection处相聚

注意点：
pa与pb的定义方式需要注意。不要用ListNdoe pa/pb，然后用pa.val != pb.val的方式；因为可能存在pa和pb不在intersection处时，值相等的情况。
直接比较pa ！= pb，这样比较的结果为pa和pb的值与指针位置均相同。



####第二次做没考虑好while循环的条件



code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        #注意pa和pb的定义方式
        pa = headA
        pb = headB
        while(pa != pb):
            if(pa):
                pa = pa.next
            else:
                pa = headB
            if(pb):
                pb = pb.next
            else:
                pb = headA
        return pa
            
