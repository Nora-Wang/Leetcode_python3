Given a node in a binary search tree, find the in-order successor of that node in the BST.

If that node has no in-order successor, return null.

The successor of a node is the node with the smallest key greater than node.val.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for Node:

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

Follow up:

Could you solve it without looking up any of the node's values?

 

Example 1:


Input: tree = [2,1,3], node = 1
Output: 2
Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.
Example 2:


Input: tree = [5,3,6,2,4,null,null,1], node = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.
Example 3:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
Output: 17
Example 4:


Input: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
Output: 15
Example 5:

Input: tree = [0], node = 0
Output: null
 

Constraints:

-10^5 <= Node.val <= 10^5
1 <= Number of Nodes <= 10^4
All Nodes will have unique values.



# 1/24/21
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        # 如果有右子树 -> 则为右子树的最左node
        if node.right:
            start = node.right
            while start.left:
                start = start.left
        # 否则，直接往parent找即可
        else:
            start = node.parent
            while start and start.val < node.val:
                start = start.parent
                
        return start





code:
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        self.result = None
        self.helper(node)
        
        return self.result
    
    def helper(self, node):
        if not node or self.result:
            return
        
        #如果有右孩子，必定在右孩子的最左
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            
            self.result = node
            return
        
        #如果没有右孩子，往它的父节点找
        node_value = node.val
        node = node.parent
        #找到第一个大于该节点的父节点
        while node and node.val < node_value:
            node = node.parent
        
        self.result = node
            
        
        
