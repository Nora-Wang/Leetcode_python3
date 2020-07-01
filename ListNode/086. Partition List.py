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

#06/30/2020
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        
        left, right = ListNode(), ListNode()
        dummy_left, dummy_right = left, right
        
        while head:
            if head.val < x:
                left.next = ListNode(head.val)
                left = left.next
            else:
                right.next = ListNode(head.val)
                right = right.next
            
            head = head.next
        
        left.next = dummy_right.next if dummy_right.next else None
        
        return dummy_left.next
    
    
    

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
        
######第二次做
        dummy_low = ListNode(None)
        low = dummy_low
        dummy_high = ListNode(None)
        dummy_high.next = head
        curt = dummy_high
        while(curt.next):
            if(curt.next.val < x):
                low.next = curt.next
                low = low.next
                curt.next = curt.next.next
                #考虑到若前一个curt在倒数第二个node时，循环一次之后curt可能会=none，这时curt.next不成立，因此加一个特判
                if not (curt):
                    break
            else:
                curt = curt.next
        low.next = dummy_high.next
        return dummy_low.next
