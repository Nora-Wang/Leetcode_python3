题目：
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

思路：
将链表向后移k次

  Given 1->2->3->4->5->NULL and k = 2,
              ↑  ↑  ↑
  slow.next=None ↑  ↑
prev.next=slow.next fast.next=head


求解步骤：
1.求链表长度l，k = l - k % l。此处k表示无论k>l or k<l,head的第k个node开始要rotate。此时fast指向最后一个node
2.用while循环，使得slow指向第k-1个node；即slow.next为rotated list的首
3.prev是一个空指针。prev.next=slow.next，slow.next=None，fast.next=head

注意：
1.[] or [1]情况的判断方法：if(head == None or head.next == None): return head
2.考虑k == l的情况，即链表向后移0次 = 整个链表不变


code:


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
######第二次做的时候没考虑到
        #特殊情况[] or [1]的判断方法
        if(head == None or head.next == None):
            return head
            
        dummy = ListNode(None)
        prev = dummy
        fast = slow = head
  ###注意此处l=1
        l = 1
        while(fast.next):
            fast = fast.next
            l += 1
            
#######第二次做的时候没考虑k>size的情况       
        #为方便后续操作，可以把k改为l-k，这样就不用利用fast,slow双指针才能找到倒数第k个数，可直接找第l-k个数
        k = l - k % l
    
#######第二次做的时候没考虑不用变的情况
        #考虑k=0 or k=nk的情况，即整个head不用改变
        if(k == l):
            return head
#######第二次做的时候写的是while(k)，但其实应该找的是3而不是4。主要原因是3后面需要清零！
        while(k - 1):
            slow = slow.next
            k -= 1
        
        prev.next = slow.next
#######第二次做的时候没考虑到，如果不将3以后的node清零，则会出现Time Limit Exceeded的情况
        slow.next = None
        fast.next = head
        return dummy.next
        
