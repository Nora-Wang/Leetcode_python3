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


时间复杂度：
O(nlogn)：满二叉树,高度logn，叶节点n/2
O(n)：所有node都排在一条线上










1.Divide and Conquer
'''
walk through all paths in tree -> save time use backtracking -> dfs recursion -> use divide and conquer

1. every level: only have left and right
2. depth: depth of tree(logn ~ n)
3. return: curt left_path, right_path (list of str)
4. end case: if not root, return

time: O(nlogn), space: O(n)

'''
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
    
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)
        
        #由于输出结果，需要注意写法，都是str
        #这里的思想是当以root点为根的leftPath已经完成，当将左node的所有path加上root后，加入result中
###编程习惯tips：注意命名的单复数
        for path in leftPaths:
            result.append(str(root.val) + '->' + str(path))
        for path in rightPaths:
            result.append(str(root.val) + '->' + str(path))
            
        #这道题做完后再将单node的情况带入，会发现多了‘->’，因此需要单独写append的格式
        if root.left == None and root.right == None:
            result.append(str(root.val))
            
        return result

2.Recursion
'''
walk through all paths in tree -> save time use backtracking -> dfs recursion
1. level: 2 child (binary tree)
2. depth: depth of tree(logn ~ n)
3. variables set: temp(record curt visited path)
4. end case: curt root is leaf, turn temp to a string, add this path to result; if not root, return

time: O(nlogn), space: O(n)

'''
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        res = []
        self.helper(root, [], res)
        
        return res
    
    def helper(self, root, temp, res):
        if not root:
            return
        
        #curt root haven't been append in temp
        if not root.left and not root.right:
            temp.append(str(root.val))
            res.append('->'.join(temp))
            #backtracking
            temp.pop()
            return
        
        temp.append(str(root.val))
        self.helper(root.left, temp, res)
        self.helper(root.right, temp, res)
        temp.pop()
        



3.Non-recursive
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
                
