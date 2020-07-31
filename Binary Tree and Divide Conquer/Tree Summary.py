#题型分析
1. 是前中后序遍历吗，是的话就用3序遍历的3种方法来做（遍历，栈，分治三种方法）
2. 是层序遍历吗，是的话就bfs，用queue
3. 是左右判断吗，是的话就分治法，但是又要分一下，是找点还是改点
   找点left = self.helper
   改点root.left = self.helper
4. 是递归回溯法吗，是的话就dfs
5. 硬解

#题目分析
1. input （recursion definition）
2. base/end case
3. recursion rules and return value（分析清楚每一层是什么,与下一层之间的联系是什么,一共有多少层）



# Recursion & divide and conquer
1. recursion和none recursion只是一种实现方式,而不是一种算法;traversal和divide and conquer都能用这两种方法实现
2. divide and conquer与recursion的区别: divide and conquer一定有返回值,而recursion一般用全局变量/类变量代替返回值

思想上的区别:
recursion本质上是指操作重复,能无限调用同一函数对数据进行处理以得到结果
traversal就是将整个tree的node给walk though一遍.主要用于判断
divide and conquer却是从上往下的遍历所有node，然后再从下往上的return所需的返回值，最后在root处得到最终结果
divide and conquer其实是一个postodrder,因为从下到上的实现

************************************
# recursion explain
    1. input （recursion definition）
    2. recursion rules（how to process next level recursion）
    3. return value
    4. base/end case
************************************

# 知识点
1. 遍历顺序
preorder traversal  根左右
inorder traversal   左根右
postorder traversal 左右根
2. Balanced binary tree, Complete binary tree, Binary Search Tree(BST)
Balanced binary tree 左右子数高度差不超过1. #leetcode 110
Complete binary tree 除了最后一层,都要满,所有节点尽量靠左 #leetcode 958
Binary Search Tree 左<=跟<右 #leetcode 98

#tips
1. iteration == None recursion
2. 每次divide and conquer的时候只要先写了not root,后续都可以直接写recursion root.left/root.right. 因为if not root,即保证了一定存在root.left/root.right
3. Backtracking == DFS
！！4. 当使用leaf节点时，一定要判断当前叶节点是否已经被加入temp中
5. 一棵树的高度O(logn) ~ O(n)
6. n个节点的binary tree一共有n个subtree(root,leaf都算)
7. tree中常用到的.join这个function，如果用于list，则需要保证list里的elements为string
