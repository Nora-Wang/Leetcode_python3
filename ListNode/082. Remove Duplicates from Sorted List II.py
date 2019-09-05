题目:
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3


思路:
dummy = ListNode(-1)
dummy.next = head
用p代表当前指针，用curt作为测试指针；当curt发现重复数据，while循环到最后一个重复数据；用p.next = curt.next进行指针的重新链接，即将重复部分删除

难点：if和while的循环条件

#第二次做的思路，该思路的时间复杂度较高
prev代表空指针，curt代表当前指针，若curt与下一个重复，将值赋给record，curt.next循环至不相等，若此时的curt.val!=curt.next.val则prev指向当前curt

##最好不要用record。record记录一下curt.val，一直循环到!=curt.val，使得prev.next = curt
##直接使用curt比较。当curt跟curt.next一样时，当curt.val == curt.next.val循环至最后一个重复数据，使得prev.next = curt.next


code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        
        while p.next:
    ###这个条件记得加上p.next.next，并且写在前面
            if(p.next.next and p.next.val == p.next.next.val):
                curt = p.next
    ###这个条件记得加上curt.next，并且写在前面
                while curt.next and curt.val == curt.next.val:
                    curt = curt.next
                p.next = curt.next
            else:
                p = p.next
                
        return dummy.next
    
    
 #######第二次做
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not (head and head.next):
            return head
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curt = head
        while(curt and curt.next):
            if(curt.val == curt.next.val):
                record = curt.val
                while(curt.val == record):
                    curt = curt.next
                    if not (curt):
                        break
            else:
                prev.next = curt
                prev = curt
                curt = curt.next
        #这句话纠结了好久。。。。不管curt最后是最后一个node还是为None，prev都需要指向它，不然就会返回head
        prev.next = curt
        return dummy.next
                
                
