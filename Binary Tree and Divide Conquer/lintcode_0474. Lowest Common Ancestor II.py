Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

The node has an extra attribute parent which point to the father of itself. The root's parent is null.

Example

Example 1:

Input：{4,3,7,#,#,5,6},3,5
Output：4
Explanation：
     4
     / \
    3   7
       / \
      5   6
LCA(3, 5) = 4
Example 2:

Input：{4,3,7,#,#,5,6},5,6
Output：7
Explanation：
      4
     / \
    3   7
       / \
      5   6
LCA(5, 6) = 7


这么简单的一道题，不要用二分法，分治法，深度优先搜索，dict，set 去重等等等
这题给了一个父指针，用到父指针才是最优解，想展示分治法，深度优先搜索技能的可以去找没父指针的LCA题去。

思路：
从A开始往root遍历一遍，记录所走路径trail。再从B往root遍历，当遇到B在trail中时，则说明A与B的lowest common ancestor为该点


code:
Version 1 31%
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        trail = [root]
        
        while A is not root:
            #如果在路上找到了B，则说明B即为lowest common ancestor
            if A == B:
                return B
            trail.append(A)
            A = A.parent
            
        while B not in trail and B is not root:
            B = B.parent
        
        return B

       
       
Version 2 96%
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        trail = [root]
        
        while A != root:
            trail.append(A)
            A = A.parent
            
        while B not in trail:
            B = B.parent
            
        return B
