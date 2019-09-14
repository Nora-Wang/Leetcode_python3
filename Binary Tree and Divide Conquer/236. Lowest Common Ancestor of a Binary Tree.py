题目：
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

3.此题还有一种变形，需要用到traverse，，且pq不一定存在在bt中
需要设定self.p_exist, self.q_exist, lca，用于判断pq是否出现，若出现，则记录其lca的值；若不出现，则返回None

1.给出node.parent，且pq一定存在在bt中
思路：
如果二叉树中存储了父亲节点，则可以从两个点出发往上寻找至root:
比如5和1：
5:[5,3]
1:[1,3]
得到路径之后从后向前遍历，3,3一样，5,1不一样了，所以最近公共祖先是3
再比如5和4：
5:[5,3]
4:[4,2,5,3]
从后向前遍历，发现3,5之后不一样了，所以公共祖先是5




2.给出root，不给parent（若两个都不给，无解），且pq一定存在在bt中
整体思路：
divide and conquer
p和q一定在分布在最后的root的left和right中，即只有情况1和4整个程序才终止；
否则对于情况2，3来说，其实就是把root改为left或right；即已经确定了LCA不在另一边中，而是在left或right中

具体思路：
如果没有存储父亲节的信息，给定root节点和两个点n1,n2:
        _______3______
       /              \
    __5__           __1__
   /     \         /     \
  6      _2_       0      8
        /   \
       7     4
n1和n2的分布情况有以下几种：
1.root=p or root=q or root=None -> 返回root
2.全在左子树 -> 返回root.left
3.全在右子树 -> 返回root.right
4.一个在左子树、一个在右子树 -> 返回root
5.这两个点不在这棵树里 -> 返回null

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #情况1
        if (root == None or root == p or root == q):
            return root
        
        #divide
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
#version1
        #conquer
        #情况4
        if left and right:
            return root
        
        #情况2
        if left and not right:
            return left
        
        #情况3
        if right and not left:
            return right
          
        #情况5
        return None

#version2
        if not left:
            return right
        if not right:
            return left
        #if left and right:
        return root
