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
        
            
            
        
            
        
