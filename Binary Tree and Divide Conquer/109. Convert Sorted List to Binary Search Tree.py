Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
 

从题目可以分析得到linked list最中间的mid_pointer是root，mid_pointer前面的是left sub_tree，mid_pointer后面的是right sub_tree,因此可以用slow + fast的方式先找到root节点
因为后续操作都是一样的，即无限分到最小subtree再将点转换为treenode连接起来，因此这里用recursion的方式解决问题
由于需要将左右子树连接到root上，因此利用divide and conquer的方式，将left_subtree_root,right_subtree_root,root相连接，即可得到最终的tree

1. input: linked list
2. recursion rules: find the root node, connect the root with left_subtree_root and right_subtree_root
3. return value: curt tree's root
4. end case: 
4.1 the linked list is None -> return None
4.2 we need to use slow and fast -> need varify fast.next -> if head.next is None, cannot find the slow and fast -> when head.next is None, return TreeNode(head.val)

 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        # slow_prev: the last node for left_linked_list
        # slow: root
        # fast: the last node for right_linked_list
        slow_prev, slow, fast = None, head, head
        while fast and fast.next:
            slow_prev = slow
            slow = slow.next
            fast = fast.next.next
        
        slow_prev.next = None
        left_list = head
        root = TreeNode(slow.val)
        right_list = slow.next
        
        root.left = self.sortedListToBST(left_list)
        root.right = self.sortedListToBST(right_list)
        
        return root
        
