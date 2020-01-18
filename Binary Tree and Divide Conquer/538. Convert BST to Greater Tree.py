题目：
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13



思路：
用sum记录右侧数据，将sum += 根，此时sum=根+右的值；运算到左时，将sum += 左，即sum = 右+根+左


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        ##注意写法，用的是root.right和root.left
        #原因：
        #root.right这个递归，是从根一直往右下走，找到最右下角的叶子位置，这个子节点是整棵树不变的那个节点
        #这道题的解法主要是要按照降序的方法去遍历这个bst，并且伴随着遍历的过程，我们要维持一个当前的sum，这个sum记录所有visited nodes的和
      ###所以遍历这个bst其实就是一个反转in-order traversal的遍历，即右根左的顺序遍历整个bst
        root.right = self.convertBST(root.right)
        
        self.sum += root.val
        root.val = self.sum
        
        root.left = self.convertBST(root.left)
        
        return root
      
      
      
更新版本:
inorder倒过来即可,需要设置一个self.sum全局变量来记录最近所得的sum,而不能直接用root.val,因为其root不一定为需要的那个值,
如下eg:4那个地方的值应该是13+5+4,而4的root却为2
              5
            /   \
           2     13
            \
             4
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.sum = 0
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        self.convertBST(root.right)
        root.val += self.sum
        self.sum = root.val
        self.convertBST(root.left)
        
        return root
