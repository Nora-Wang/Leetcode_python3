题目：
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 

          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.



思路：
注意理解题意最长是4-2-1-3，所以应该是将求左右两边的高度相加


code：
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.count_diameter(root)
        return self.res
        
    def count_diameter(self, root):
        
        if not root:
            return 0

        left_count = self.count_diameter(root.left)
        right_count = self.count_diameter(root.right)
        
        #如果左侧有node，则高度+1
        if root.left:
            left_count += 1

        if root.right:
            right_count += 1
            
        #这里要注意在求self.res时，还需要与self.res自己比较大小
        #
        self.res = max(self.res, left_count + right_count)
        
        #返回当前node的高度
        return max(left_count, right_count)


#simple version
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.count_diameter(root)
        return self.res
        
    def count_diameter(self, root):
        
        if not root:
            return 0

        left_count = self.count_diameter(root.left)
        right_count = self.count_diameter(root.right)

        #不需要判断是否有左右节点是因为循环到叶节点.next时，为0；倒数第二层，即叶节点时，为1
        #换句话说，对于root1，左子树left_count=1，
        #此时右子树没有left和right，return max(left_count, right_count) + 1，可使得右子树right_count直接=1
        self.res = max(self.res, left_count + right_count)
        
        return max(left_count, right_count) + 1
        
        
