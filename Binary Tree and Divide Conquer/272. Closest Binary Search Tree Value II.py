Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?



1. O(h + k)的时间复杂度。h为树的高度，平均为logn。

【确认条件】
（1）沟通BST的定义。
（2）确认是否需要判断tree和k是否valid。
（3）确认不会存在两个与target距离相等的值，否则输出list的时候还得判断哪一个放在前面。
（4）确认k是否小于等于tree中的节点数（虽然解法中遇到这种情况会通过break跳出）。

【解题思路】
（1）通过get_stacks()虚拟寻找target的插入位置，并将一路上经过的点根据值的大小分别放入self.prev_stack和self.next_stack。
用两个栈的好处是：之后在实现get_next()和get_prev()的时候会相对简单一些，不需要像完整版BST iterator那么复杂。

（2）实现get_next()，利用next_stack寻找next_value。
在一般的BST iterator中，寻找下一节点的算法是：如果当前点存在右子树，那么就是右子树中一直向左走到底的那个点；
如果当前点不存在右子树，则对到达当前点的路径进行反向遍历（一直pop stack），寻找第一个（离当前点最近的）左拐的点。
然而在本题中，因为已经分离prev_stack和next_stack，所以在当前节点不存在右子树的情况下，当前节点在next_stack中的前一个位置自然就是要找的下一个点。
因此代码中只需处理当前节点存在右子树时的情况，即先取当前节点的右子树，再一路向左走到底。

（3）实现get_prev()，利用prev_stack寻找prev_value。
对get_next()的处理方式取反，即先取当前节点的左子树，再一路向右走到底。
若不存在左子树，在pop出当前节点后，stack[-1]自然处于下一个prev节点的位置。

（4）for循环k次，每次比较prev_stack和next_stack栈顶节点的值，把与target距离近的那个放进results中。

【实现要点】
（1）实现get_stacks()的时候，在把节点分入两个栈的时候注意思考一下，别把大小写，左右子树弄反了。
    另外对于本题，不需要对root.val == target的情况专门处理。
（2）实现get_next()和get_prev()注意细节（完整版BST iterator其实需要背诵，本题中再对其简化）。
（3）比较大小的时候引入sys.maxsize作为异常情况处理。

【复杂度】
时间复杂度：O(h + k)，O(h)来自于对树的搜索，O(k)是获取k个结果。
空间复杂度：O(h)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root or k == 0:
            return []
        #记录最后结果
        result = []
        
        #记录大于target的值self.next_stack；小于target的值self.prev_stack
        self.next_stack, self.prev_stack = [], []
        
        #获取self.next_stack, self.prev_stack
        self.get_stacks(root, target)
        
        #得到k个挨target最近的值
        for _ in range(k):
            #当所有node都被遍历过了
            if len(self.next_stack) == 0 and len(self.prev_stack) == 0:
                break
                
            #当已经不存在比target小的数时，用sys.maxsize做next_diff的值，这样next_diff一定大于prev_diff，最后会取prev_diff的值
            if len(self.next_stack) == 0:
                next_diff = sys.maxsize
            else:
                next_diff = abs(self.next_stack[-1].val - target)
                
            #当已经不存在比target大的数时，用sys.maxsize做prev_diff的值，这样next_diff一定小于prev_diff，最后会取next_diff的值
            if len(self.prev_stack) == 0:
                prev_diff = sys.maxsize
            else:
                prev_diff = abs(self.prev_stack[-1].val - target)
                
            #比较前一个数和后一个数谁更接近target，将更接近的加入result
            if next_diff > prev_diff:
                result.append(self.prev_stack[-1].val)
                self.get_prev()
            else:
                result.append(self.next_stack[-1].val)
                self.get_next()
                
        return result
    
    #生成两个stack，用于记录大于target的值self.next_stack，小于target的值self.prev_stack
    #注意：在比target大的数中，只取node.left，这样值会更为接近target；小于target的数同理
    def get_stacks(self, root, target):
        while root:
            if root.val > target:
                self.next_stack.append(root)
                root = root.left
            else:
                self.prev_stack.append(root)
                root = root.right
    
    #取得当前target的前一个node的值，即self.prev_stack的最后一个数，并将self.prev_stack作出改变
    #这里需要将node.left的向右延伸的所有right nodes加入self.prev_stack，因为在def get_stacks(self, root, target)中只将node和node.right加进去了
    #由于right node已经全部被加入pre_stack,且已经被pop出,现在只剩下当前node.left的所有数;这时最接近target的应该为当前node.left一直向右走到底的node
    def get_prev(self): 
        node = self.prev_stack.pop().left
        
        while node:
            self.prev_stack.append(node)
            node = node.right
    
    def get_next(self):
        node = self.next_stack.pop().right
        
        while node:
            self.next_stack.append(node)
            node = node.left
