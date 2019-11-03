题目：
Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

Example

Example 1:

Input:
{1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
1   2 -4  -5 
The sum of whole tree is minimum, so return the root.
Example 2:

Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
Notice

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.



Divide Conquer + Traverse

class Solution:
    def findSubtree(self, root):
    #注意刚开始的min_sum的取值，系统最大值
      self.min_sum = sys.maxsize
      self.min_sum_root = None
      findsum(root)
      
      return self.min_sum_root
    
    def findsum(self,root):
      if not root:
        return None
        
      #divide conquer
      left = findsum(root.left)
      right = findsum(root.right)
      cur_sum = left.val + right.val + root.val
      
      #traverse(compare with global variable与全局变量做比较，self.min_sum，self.min_sum_root)
      if(cur_sum < self.min_sum):
        self.min_sum = cur_sum
        self.min_sum_root = root
        
      #个人觉得return ,也行
      return cur_sum
        
