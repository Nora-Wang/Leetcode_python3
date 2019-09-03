题目：
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5


思路：
将链表排成两队，小于x的一队，大于等于x的一队，然后把两个链表连起来。

链表的结构会发生变化，所以需要两个dummy node，一个用来指向小的队dummy_low，一个用来指向大的队dummy_high。

解题步骤：

遍历数组，将比x小的元素放到dummy_low队伍后面，将比x大的元素放到dummy_high队伍后面
结束后将两个链表连接起来：此时dummy_low的最后一个node为curt_low，其指向dummy_high.next
将链表结尾置空：tail.next = null,否则会保留原始节点的next。
返回dummy_low.next;



code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy_high = ListNode(None)
        prev_high = dummy_high
        dummy_low = ListNode(None)
        dummy_low.next = head
        curt_low= dummy_low
        temp = head
        while(temp):
            if(temp.val < x):
                curt_low.next = temp
                curt_low = curt_low.next
            else:
                prev_high.next = temp
                prev_high = prev_high.next
            temp = temp.next
        curt_low.next = dummy_high.next
        #将链表结尾置空：tail.next = null,否则会保留原始节点的next。
        prev_high.next = None
        return dummy_low.next
        
