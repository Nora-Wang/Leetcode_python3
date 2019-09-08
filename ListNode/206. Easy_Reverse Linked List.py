题目：
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL



思路：设计3个node prev, curt, temp
temp = curt.next
curt.next = prev
prev = curt
curt = temp

 null   [1,] -> [2,] -> [3,] -> [4,] -> [,5,]
  ↑       ↑
 prev   curt
 
1. 用temp记录下curt.next（因为后面要修改curt.next）
 null   [1,] -> [2,] -> [3,] -> [4,] -> [,5,]
  ↑       ↑      ↑
 prev   curt    temp
 
2. 将curt.next指向其前序节点prev，此时原来的后续链断掉:
 null <- [1,]  [2,] -> [3,] -> [4,] -> [,5,]
  ↑       ↑      ↑
 prev   curt    temp
 
3. 将prev移到curt位置，curt移动到原来的curt.next,即temp:
null <- [1,]  [2,] -> [3,] -> [4,] -> [,5,]
         ↑      ↑       ↑
        prev   curt    temp




code:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
######第二次做的注意点！！！
        #注意不要用prev = ListNode(None)；因为这样prev就算一个node，最后的结果：5->4->3->2->1->None；正确结果：5->4->3->2->1
        prev = None
        curt = head
        while(curt):
            temp = curt.next
            curt.next = prev
            prev = curt
            curt = temp
        return prev
