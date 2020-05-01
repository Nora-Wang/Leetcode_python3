Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

            
            
#反向postroder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        #prev相当于是当前root的左子树
        self.prev = None
        
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        #将左子树放在root的右侧
        root.right = self.prev
        #将左子树清空
        root.left = None
        #更新root
        self.prev = root
            
            
            
            
            
            
            
            
            
            
            
            
          
思路：
1.将4复制到3.right处
    1
   / 
  2   
 / \  
3   4 
 \  
  4
2.将2.left copy到2.right处
    1
   / 
  2   
 / \  
3   3
 \   \
  4   4
3.将2.left清空
    1
   / 
  2   
   \  
    3
     \
      4
此时即完成了flatten以2为root的binary tree
            
'''
use divide and conquer
1. definition: lastnode = helper(root)
2. rules: 
root.left exist: left lastnode.right = root.right, root.right = root.left, root.left = None; curt lastnode = right lastnode
root.left exist, root.right not exist: copy root.left to root.right, root.left = None, curt lastnode = left lastnode
both left/right not exist: lastnode = root
3. base case: not root, return None
4. return: curt lastnode

time: O(n), space:O(n)
'''
code:
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        if not root:
            return root
            
        left_last = self.flatten(root.left)
        right_last = self.flatten(root.right)
        
        #此时left_last为3，right_last为4
        if left_last:
            #思路中的3步
            left_last.right = root.right
            root.right = root.left
            root.left = None
            
        #返回当前root.right的最下面的点
        #此时最下面的点为4，即right_last
        #当不存在right_last时，即原始树中为[1,2,#,3,#]的情况时，最下面的点为3，即left_last
        #当left_last和right_last都不存在时，说明此刻只剩下root了，直接返回root即可
#因为对于下一个循环来说，这一个循环相当于是将其root.left flatten了，只有将最后一个点返回才能将root.right继续接在root.left上，然后再继续flatten
        return right_last or left_last or root
        
            
            
最后的return中三个值放置顺序的解释:
        /      
      root      
    /      \
root.left   B
   \        
    A

1. AB都存在/只存在B:此时left_last=A,right_last=B,将Bcopy到A.right,再将root.left放到root.right处,此时root.right的最后一个node为B,即right_last
2. 只存在A:直接将root.left挪到root的right处,此时最后一个为A,即left_last
3. AB都不存在:直接返回root即可
