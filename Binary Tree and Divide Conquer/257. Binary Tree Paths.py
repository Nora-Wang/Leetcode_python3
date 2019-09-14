题目：
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3




1.Divide and Conquer
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        #不能return None，因为整个结果是一个list，应该返回一个空list
        if not root:
            return []
    
        leftPath = self.binaryTreePaths(root.left)
        rightPath = self.binaryTreePaths(root.right)
        
        #由于输出结果，需要注意写法，都是str
        #这里的思想是当以root点为根的leftPath已经完成，当将左node的所有path加上root后，加入result中
###编程习惯tips：注意命名的单复数
      for paths in leftPaths:
            result.append(str(root.val) + '->' + str(paths))
        for paths in rightPaths:
            result.append(str(root.val) + '->' + str(paths))
            
        #这道题做完后再将单node的情况带入，会发现多了‘->’，因此需要单独写append的格式
        if root.left == None and root.right == None:
            result.append(str(root.val))
            
        return result

   
2.Non-recursive(traversal)
从上到下一个stark就可以，注意第一次传入的是空string
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
      #判断root
        if not root:
            return []
        result = []
      #重点：stark的定义方式[(node, path)]
        stark = [(root, '')]
         
        while stark:
            node, path = stark.pop()
            
            #如果是第一个节点，其path为空，则不需要‘->’
            if path:
                path += '->' + str(node.val)
            else:
                path += str(node.val)
            
            #判断是否到叶节点，如果是则将path加入result；并结束此次循环
            if node.left is None and node.right is None:
                result.append(path)
                continue
               
            #如果有右节点，则将其push进stark；如果有左节点，则同样push进stark
            #下一次的循环就是先查找左节点的path，等左节点path已经全部找完，再寻找右节点的path
            if node.right:
                stark.append((node.right, path))
            if node.left:
                stark.append((node.left, path))
            
                
        return result
                
