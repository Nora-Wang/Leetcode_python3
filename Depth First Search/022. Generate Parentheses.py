Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

# 08/01/2020
# DFS Version
                                Empty
                           /            \
Position 0                (              )
                        /   \          /    \
Position 1             (     )        (      )
                     /   \
Position 2
…….     
# time: O(n * 2^n), space: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        self.dfs(n, 0, 0, [], res)
        
        return res
    
    # left = 左括号的个数，right = 右括号的个数
    def dfs(self, n, left, right, temp, res):
	# end case
        if left == n and right == n:
            res.append(''.join(temp))
            return
        
	# 只要left < n，就能加入'('
        if left < n:
            temp.append('(')
            self.dfs(n, left + 1, right, temp, res)
            temp.pop()
        
	# 只要right < left，就能加入')'
        if left > right:
            temp.append(')')
            self.dfs(n, left, right + 1, temp, res)
            temp.pop()





3连问:
1.每一层都代表什么，或者什么状态？
     whether to add ( or )
 2.有多少层？
			2 * N levels
 3. 在遍历空间中的每一层，有多少种状态/分支，或者说对于其中一个节点，它可以衍生出来哪些下一层的节点？
    2 branches, add (, add)
    
这道题用left和right来记录左括号和右括号的个数,以此限制结果是valid的:只有当left > right时,才能加左括号(思路很像大小堆那道题)
    
Time complexity = O(2^(N))#二叉树,一共n*2层
Space complexity = O(N*2^N)#二叉树,一共n*2层,因此一共有2^(n*2)种结果,而每个结果的长度为2*n -> (2*n) * 2^(n*2) = O(N*2^N)

code:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        
        res = []
        self.dfs(n, 0, 0, [], res)
        
        return res
    
    
    def dfs(self, n, left, right, temp, res):
        #end case
        if left == n and right == n and len(temp) == n * 2:
            res.append(''.join(temp))
        
        #注意left和right < n
        if left < n:
            temp.append('(')
            self.dfs(n, left + 1, right, temp, res)
            temp.pop()
        
        if right < n and right < left:
            temp.append(')')
            self.dfs(n, left, right + 1, temp, res)
            temp.pop()
            
        
        
