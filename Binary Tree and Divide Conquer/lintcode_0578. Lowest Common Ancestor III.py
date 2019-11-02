Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.
The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return null if LCA does not exist.

Example

Example1

Input: 
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7 
5 8
Output: 
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null

Example2

Input:
{1}
1 1
Output: 
1
Explanation:
The tree is just a node, whose value is 1.
Notice

node A or node B may not exist in tree.
Each node has a different value


divide and conquer
两个given node，A, B
helper函数在遇到A或B的时候即返回它;
如果左右node的返回值都不为空，即说明当前node为LCA，返回当前node;这样可以解决两node其中之一是LCA的情况，直接返回left或right
考虑到有可能LCA不存在(即A或B不存在于root中)，这里设定两个boolean分别表示A或B是否存在于root中，如果最终两者不全为true，则返回null。

code:
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        if not root:
            return None
            
        is_exist_A, is_exist_B, LCA = self.helper(root, A, B)
        
        #只有当A和B在遍历过程中发现确实存在于root中，才能说明确实存在LCA
        if is_exist_A and is_exist_B:
            return LCA
            
        return None
        
    def helper(self, root, A, B):
        #分治出口
        if not root:
            return False, False, root
            
        #初始化，AB此时都不存在
        #用于记录A和B是否存在于root中
        is_exist_A = False
        is_exist_B = False
        
        left_is_exist_A, left_is_exist_B, left_node = self.helper(root.left, A, B)
        right_is_exist_A, right_is_exist_B, right_node = self.helper(root.right, A, B)
        
        #记录A和B是否被遍历到
        if left_is_exist_A or right_is_exist_A or root == A:
            is_exist_A = True
        if left_is_exist_B or right_is_exist_B or root == B:
            is_exist_B = True
                            
        #当该点就是A或B时，返回root
        #要先写这部分 
        #eg:{2,-1},-1,2 若后写，则输出为-1
        if root == A or root == B:
            return is_exist_A, is_exist_B, root
        
        #AB分别存在于left和right中时，返回root
        if left_node and right_node:
            return is_exist_A, is_exist_B, root
        #当只存在于left或right中时
        #由于前面判断过left_node and right_node的情况，因此只剩下单独存在于left/right的情况
        if left_node:
            return is_exist_A, is_exist_B, left_node
        if right_node:
            return is_exist_A, is_exist_B, right_node
            
        return is_exist_A, is_exist_B, None
            
