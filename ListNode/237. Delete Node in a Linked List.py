题目：
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.


思路：
注意由于是单链表node，即所给数据是从node开始的一个单链表。例：head = [4,5,1,9], node = 5；而def deleteNode(self, node)中的node=[5,1,9]
其不能找前驱节点，所以不能按常规方法将该节点删除。

可以换一种思路，将下一个节点的值复制到当前节点，然后将下一个节点删除即可。

时间复杂度分析：只有常数次操作，所以时间复杂度是 O(1)。




code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
