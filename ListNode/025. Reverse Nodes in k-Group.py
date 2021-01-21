题目：
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.



思路：
这道题很难，思路其实还好，主要是写代码的时候有很多注意事项

主要思路：将整个head分为每段为k个node的子链表(不够k可不变)，然后reverse每个n1...nk子链表



# 1/21/21
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
prev -> curt -> ... -> curt_tail -> next_head
prev -> curt_tail -> ... -> curt -> next_head

'''
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        
        dummy = prev = ListNode()
        curt = dummy.next = head
        
        while curt:
            if not self.is_valid(curt, k):
                return dummy.next
            
            # else
            curt_tail, next_head = self.swap(curt, k)
            
            prev.next = curt_tail
            curt.next = next_head
            
            prev = curt
            curt = next_head
        
        return dummy.next
    
    # 这里注意：并没有将curt另外取名赋值，是因为在helper function中，对于linkedlist参数的改变并不会对原始数据进行改变
    # 即，curt在经过了is_valid和swap function后，回到reverseKGroup函数中，还是原来的数据，不会因helper function的改变而改变 (局部和全局的差异)
    def is_valid(self, curt, k):
        length = 0
        
        while curt and length < k:
            curt = curt.next
            length += 1
        
        return length == k
    
    def swap(self, curt, k):
        prev = None
        
        for _ in range(k):
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
            
        return prev, curt







code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #prev n1 n2   ... nk nk+1...
        #prev nk nk-1 ... n1 nk+1...
        #return n1
        #head is not None
        def reverseKNode(node, k):
            #便于connect；记录一下n1前一个node
            start = node
            #赋值问题：考虑清楚，node是n1前一个node
            n1 = nk = node.next
            #要为k-1，否则会循环至nk+1处
            
 ###########这段很迷。。。。需要两次判断if not (nk)，少一次都不行
#######第二次做的时候也没写第二个判断
            while(k - 1):
                nk = nk.next
            #第一次：当剩余node不足k个时，直接退出，不用reverse
                if not (nk):
                    return None
                k -= 1
            #第二次
            if not (nk):
                return None
            #便于connect；记录一下nk后一个node
            nextstart = nk.next
            
            #reverse
            prev = ListNode(None)
            curt = n1
            #注意：reverse的模板结束的结果为
            #prev = nk，curt = nk.next， temp = nk，next.next
            #因此while循环的判断依据为nextstart
  #####第二次做的时候，将while循环的条件写成了k，但其实这时的k已经在寻找nk的时候变了
            while(curt != nextstart):
                temp = curt.next
                curt.next = prev
                prev = curt
                curt = temp
                
            #将reverse部分与node重新connect
            start.next = nk
            n1.next = nextstart
            return n1
        
        
        dummy = ListNode(None)
        dummy.next = head
        
        #用while循环的方式将node分成每段为k个node的链表
        #注意：此处的node是每个n1...nk的前一个node，即n1前一个node；且每次reverseKNode函数返回的都是n1，即下一次循环的前一个node
        node = dummy
 #####第二次写的时候纠结了好久while循环里写什么条件，原因是认为node=None，但其实node=None+head，所以第一次循环的时候是
        while(node):
            node = reverseKNode(node, k)
        return dummy.next
            
        

        
