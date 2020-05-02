Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  
Clarification:

Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.

The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:

   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].

#05/02/2020                                        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
to the most left and depthest node, use stack to record the path
pop one(-> become right child), varify whether it has right child(-> become left child), continue pop to the next loop

time: O(n), space: O(n)
'''

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        curt = dummy = TreeNode(None)
        
        while stack:
            root = stack.pop()
            curt.right = TreeNode(root.val)
            if root.right:
                curt.left = TreeNode(root.right.val)

            curt = curt.right
        
        return dummy.right
                               
                                        
                                        
                                        
                                        
                                        
                                        
                                        
                                        

code:
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        return self.helper(root)
        
    def helper(self, root):
        #找到最左边的node,直接返回,将其作为新tree的node
        if not root.left:
            return root
        
        #先把左子树递归好
        new_root = self.helper(root.left)
        
        #按照题意改变根左右的值
        #这里不能用new_root,因为除了第一次循环的时候root.left == new_root,其它时候相当于是new_root的roots;
        #并且new_root是新tree的root,因此不能被改变,需要记录和返回
        root.left.right = root
        root.left.left = root.right
        
        #根左右的值（清空）断开
        root.left = None
        root.right = None
        
        #这里返回的是new_root,即一直都是一开始的最左的那个node
        return new_root
