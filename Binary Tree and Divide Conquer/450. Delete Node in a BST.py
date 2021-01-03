Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
    
    
    
# 1/2/2021
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        parent_node, direction, key_node = self.find_key(root, key)

        # not exist
        if not key_node:
            return root

        # connect key_node.right and key_node.left
        if key_node.right:
            sub_head = curt = key_node.right
            while curt.left:
                curt = curt.left
            curt.left = key_node.left
        else:
            sub_head = key_node.left
        
        # without parent_node
        if not parent_node:
            return sub_head

        # connect sub_head and parent_node
        if direction == 'l':
            parent_node.left = sub_head
        else:
            parent_node.right = sub_head

        return root

    def find_key(self, root, key):
        parent_node, direction = None, None

        while root:
            if root.val == key:
                return parent_node, direction, root
            
            parent_node = root
            if key > root.val:
                root = root.right
                direction = 'r'
            else:
                root = root.left
                direction = 'l'
        
        return None, None, None
              
        



    
    
    
    
    
code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1. find the node
based on BST property to find the key node -> key > root.val, go root.right; else, go root.left, use prev to record node.parent

if not find: return root

2. delete the node
if node has right child: go to right child's most left node, put left child to this node, and then put prev.left/right = right child

if node do not has right child: put left child to the prev.left/right

if do not have both left/right child: prev.left/right = None

3. edge cases:
3.1 key exist?
3.2 need a flag to determine add the new subtree to prev's left or right
3.3 saperate delete node to 2 cases: key_node.right exist or not? (if yes, merge key_node.left to the key_node.right; if no, duplicate key_node.left to key_node.right)
3.4 key is the root, which means cannot find prev

time: O(h), space: O(h)
'''
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        
        is_exist, prev, direct, key_node = self.find_key(root, key)
        
        if not is_exist:
            return root
        
        #delete the node
        #merge all nodes to key_node.right subtree
        if key_node.right:
            right = key_node.right
            while right.left:
                right = right.left
            right.left = key_node.left
        else:
            key_node.right = key_node.left
        
        #key_node is the root -> root.right become the new root
        if not prev:
            return key_node.right
        else:
            #otherwise, based on the parent_to_key_direct to renew the tree
            if direct == 'right':
                prev.right = key_node.right
            else:
                prev.left = key_node.right
        
        return root
        
    def find_key(self, root, key):
        is_exist = False
        prev = None
        parent_to_key_direct = None
        key_node = None
        
        while root:
            if root.val == key:
                is_exist = True
                key_node = root
                return is_exist, prev, parent_to_key_direct, key_node
            
            prev = root
            if root.val < key:
                parent_to_key_direct = 'right'
                root = root.right
            else:
                parent_to_key_direct = 'left'
                root = root.left
                
        return is_exist, prev, parent_to_key_direct, key_node
