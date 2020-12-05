Given the root of a binary tree, return the lowest common ancestor (LCA) of two given nodes, p and q. If either node p or q does not exist in the tree, return null. All values of the nodes in the tree are unique.

According to the definition of LCA on Wikipedia: "The lowest common ancestor of two nodes p and q in a binary tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)". A descendant of a node x is a node y that is on the path from node x to some leaf node.

 

Example 1:


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
Example 2:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5. A node can be a descendant of itself according to the definition of LCA.
Example 3:



Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 10
Output: null
Explanation: Node 10 does not exist in the tree, so return null.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
Follow up: Can you find the LCA traversing the tree, without checking nodes existence?
 
Version 1
# 利用Leetcode 236
# 不同点：It is NOT guaranteed that both p and q are in the tree.
# -> 1. 需要判断p、q是否出现
# -> 2. We need to traverse the entire tree even after we've found one of them. 
#       而Leetcode 236则是we can return either p OR q as soon as we find one of them
#       原因：In 1644, if you return early, the above example would be null, because the code stops when it finds 5 and does not keep searching for 4.

Version 1 # Use boolean as flags
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.has_p = False
        self.has_q = False
        res = self.helper(root, p, q)
        
        return res if self.has_p and self.has_q else None
    
    def helper(self, root, p, q):
        if not root:
            return root
        
        left = self.helper(root.left, p, q)
        right = self.helper(root.right, p, q)
        
        # 不同点2 -> 需要在最后进行判断，不能在recursion之前
        if root == p:
            self.has_p = True
            return root
        if root == q:
            self.has_q = True
            return root
        
        if left and right:
            return root
        
        return left if left else right

Version 2 # Use integers as flags
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        count = [0]
        res = self.helper(root, p, q, count)
        
        return res if count[0] == 2 else None
    
    def helper(self, root, p, q, count):
        if not root:
            return root
        
        left = self.helper(root.left, p, q, count)
        right = self.helper(root.right, p, q, count)
        
        # 同样要放recursion的后面
        if root == p or root == q:
            count[0] += 1
            return root
        
        if left and right:
            return root
        
        return left if left else right
 
 
Version 0 # 自己做的方法，思路类似is balanced tree，同Version 1 Use boolean as flags
# 判断p和q是否有出现
# 因为用的divide and conquer，即down-top，一旦出现满足p和q同时出现，就用self.res记录，则能找到LCA
# time: O(n), space: O(n)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        self.helper(root, p, q)

        return self.res

    def helper(self, root, p, q):
        if not root:
            return False, False

        l_p, l_q = self.helper(root.left, p, q)
        r_p, r_q = self.helper(root.right, p, q)

        has_p = l_p or r_p or root == p
        has_q = l_q or r_q or root == q
        
        # 这里需要mark一下self.res已经出现了 -> return False, False
        # 这里是利用了All Node.val are unique -> 出现后直接return False，由于是unique的，因此其它地方也不会再replace self.res的值
        if has_p and has_q:
            self.res = root
            return False, False

        return has_p, has_q 
 
 
 



