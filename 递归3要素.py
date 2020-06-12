1. 递归的定义
每一个递归函数，都需要有明确的定义，有了正确的定义以后，才能够对递归进行拆解。
#接受什么参数，返回什么值，代表什么意思

2. 递归的拆解
一个大问题如何拆解为若干个小问题去解决。
#每次递归都是为了让问题规模变小
eg:
先把 root 放到 result 里 --> result.add(root);
再把左子树的前序遍历放到 result 里 --> preorder(root.left, result)。回想一下递归的定义，是不是正是如此？
再把右子树的前序遍历放到 result 里 --> preorder(root.right, result)。

3. 递归的结束
什么时候可以直接知道答案，不用再拆解，直接 return
#必须有一个明确的结束条件


recursion的分析步骤:
1. input （recursion definition）
2. base/end case
3. recursion rules（how to process next level recursion）
4. return value

时间复杂度分析:
想像一棵树
1. 一共有多少层
2. 每一层代表什么
