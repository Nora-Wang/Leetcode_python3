Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.  (The values of the nodes may still be duplicates.)

Left boundary is defined as the path from root to the left-most node. Right boundary is defined as the path from root to the right-most node. If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. Note this definition only applies to the input binary tree, and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same way with left and right exchanged.

Example 1

Input:
  1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
So order them in anti-clockwise without duplicates and we have [1,3,4,2].
 

Example 2

Input:
    ____1_____
   /          \
  2            3
 / \          / 
4   5        6   
   / \      / \
  7   8    9  10  
       
Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4. (4 is the left-most node according to definition)
The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have [1,2,4,7,8,9,10,6,3].

code:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        #edge case的处理
        #此时leaves = [root.val], left_boundary = [root.val], right_boundary = [];因此结果为[root.val, root.val]出现重复
        if not root.left and not root.right:
            return [root.val]
        
        left_boundary = [root.val]
        self.get_left_boundary(root.left, left_boundary)
        #print(left_boundary)
        
        leaves = []
        self.get_leaves(root, leaves)
        #print(leaves)
        
        right_boundary = [root.val]
        self.get_right_boundary(root.right, right_boundary)
        #print(right_boundary)
        
        #这题的重点是有很多点需要注意
        #1. right_boundary的结果是反向输出的
        right_boundary.reverse()
        
        #2. 如何将结果输出
        #思考题目的结果,可以看出
        #left_boundary = root + path + leaf
        #right_boundary = leaf + path + root
        #leaves就是所有leaf
        #因此组合一下就是将right_boundary去头去尾 + left_boundary去尾 + leaves
        right_boundary = right_boundary[1:-1]
        
        #这里有个edge case,即当root.left不存在时,left_boundary = [root.val],这时再去尾的话,root也没了;因此需要判断一下left_boundary的长度
        if len(left_boundary) > 1:
            left_boundary = left_boundary[:-1]
        
        res = []
        res.extend(left_boundary)
        res.extend(leaves)
        res.extend(right_boundary)
        
        return res
    
    def get_left_boundary(self, root, left_boundary):
        if not root:
            return
        
        left_boundary.append(root.val)
        
        if not root.left and not root.right:
            return
        
        if root.left:
            self.get_left_boundary(root.left, left_boundary)
        else:
            self.get_left_boundary(root.right, left_boundary)
            
    def get_leaves(self, root, leaves):
        if not root:
            return
        
        if not root.left and not root.right:
            leaves.append(root.val)
            return
        
        self.get_leaves(root.left, leaves)
        self.get_leaves(root.right, leaves)
    
    def get_right_boundary(self, root, right_boundary):
        if not root:
            return
        
        right_boundary.append(root.val)
        
        if not root.left and not root.right:
            return
        
        if root.right:
            self.get_right_boundary(root.right, right_boundary)
        else:
            self.get_right_boundary(root.left, right_boundary)
            
