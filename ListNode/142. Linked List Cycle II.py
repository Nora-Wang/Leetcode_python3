题目：
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

思路：
1.先按照slow走一步fast走两步的过程找到相遇点
2.fast从快慢指针相遇的地方出发，slow指针从初始地方head出发，两个指针每次走一步，直到相遇，就是环的入口

注意：
用下面语句先排除不是循环的情况（pos=-1），时间节省很多
if not(fast and fast.next):
    return None
    
#若是circle，fast和fast.next一定在circle内无限循环，不应该出现None的情况
#fast和fast.next两个都要判断（理由同上面的while循环）
        



code:

时间复杂度较优解法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                break
                
        #排除不是循环的情况（pos=-1）
        #若是circle，fast和fast.next一定在circle内无限循环，不应该出现None的情况
        #fast和fast.next两个都要判断（理由同上面的while循环）
        if not(fast and fast.next):
            return None
        
        slow = head
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return slow
                
#解法2      
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = finder = head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if(fast == slow):
                while(finder != fast):
                    finder = finder.next
                    fast = fast.next
                return finder
        return None
