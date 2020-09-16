思考步骤：
1. 在遍历空间中，每一层都代表什么，或者什么状态？
2. 在遍历空间中，有多少层？
3. 在遍历空间中的每一层，有多少种状态/分支，或者说对于其中一个节点，它可以衍生出来哪些下一层的节点？


时间复杂度：
#DFS时间复杂度通用公式：
#O(答案个数 * 构造每个答案的时间)

1.搜索的时间复杂度：O(答案总数 * 构造每个答案的时间)
举例：Subsets问题,即Combinations，求所有的子集。子集个数一共 2^n(每一个点都有两个选择,选or不选,一共有n个点)，每个集合的平均长度是 O(n) 的，
所以时间复杂度为 O(n * 2^n)
同理 Permutations 问题的时间复杂度为：O(n * n!)(每个点都必须被选到,全部选完的总机率为n!)

2.动态规划的时间复杂度：O(状态总数 * 计算每个状态的时间复杂度)
举例：triangle，数字三角形的最短路径，状态总数约 O(n^2) 个，计算每个状态的时间复杂度为 O(1)——就是求一下 min。所以总的时间复杂度为 O(n^2)

3.用分治法解决二叉树问题的时间复杂度：O(二叉树节点个数 * 每个节点的计算时间)
举例：二叉树最大深度。二叉树节点个数为 N，每个节点上的计算时间为 O(1)。总的时间复杂度为 O(N)


permutation和combination都算subset的子问题，dfs可以做到找到所有可能解，里面的实现细节就是各式各样的去重。
图上的搜索，不仅可以用bfs，也可以用dfs，有时候可以衡量一下递归深度对时间复杂的的影响，然后权衡dfs还是bfs

除了二叉树以外的 90% DFS的题，要么是排列，要么是组合
找到图中的所有满足条件的路径用DFS
路径 = 方案 = 图中节点的排列组合 
很多题不像二叉树那样直接给你一个图(二叉树也是一个图) 
点、边、路径是需要你自己去分析的

eg:
1. Combinations(Subsets)
点:集合中的元素
边:元素与元素之间用有向边连接，小的点指向大的点(为了避免选出 12 和 21 这种重复集合) 
路径:= 子集 = 图中任意点出发到任意点结束的一条路径
T(n) = O(2^n * n)
问题模型:求出所有满足条件的“组合”。 
判断条件:组合中的元素是顺序无关的。 
时间复杂度:与 2^n 相关。
  
方法1:
# 时间为O(2^n)
# 空间为O(n)
empty                                            {}
                                     /                     \
For a                              {a}                      {}
                              /          \             /         \ 
For b                     {a, b}         {a}         {b}         {}
                         /      \       /    \       /   \      /   \
For c             {a, b, c}  {a, b}  {a, c}  {a}    {b,c} {b}   {c}  {}

方法2:
# 时间为O(2^n)
# 空间为O(n)
Empty                     {}
选1个     a         b           c          {}
选2个 ab   ac      bc   
选3个 abc

'''
方法2 code:
def combination(self, candidates, target):
        results = [] #定义结果
        
        #当后续有candidates[i]与candidates[i - 1]的比较时,需要sort
        #candidates.sort()
        
        #DFS的temp都是以空数组/空string开头进行调用的
        self.dfs(candidates, 0, [], results, target) 
        
        return results
        
    #recursion definition     
    def dfs(self, candidates, start_index, temp, results, cur_target): 
        #recursion end case
        #!!!!!!!!!记得写return

        #题目给的限制条件:
            #return results.append(list(temp))
        if cur_target < 0:
            return
        if cur_target == 0: 
						#deep copy
            results.append(list(temp))
						return 

        #recursion explanation
        #镜像对称
        for i in range(start_index, len(candidates)): 
            #去重判断(1,2')与(1,2'')
            #if i > start_index and nums[i] == nums[i - 1]:
								#continue
            
            temp.append(candidates[i])#元素写入temp [2]->[2,2]
            #注意i or i + 1
            self.dfs(candidates, i, temp, results, cur_target - candidates[i])
            temp.pop()#弹出元素（因为用过了） [2,2]->[2]
'''

2. Permutations
点:每个数为一个点
边:任意两两点之间都有连边，且为无向边
路径:= 排列 = 从任意点出发到任意点结束经过每个点一次且仅一次的路径
T(n) = O(n! * n)
问题模型:求出所有满足条件的“排列”。 
判断条件:组合中的元素是顺序“相关”的。 
时间复杂度:与 n! 相关。
# 时间为O(n!)
# 空间为O(n)
Empty                     {}
选1个     a           b           c          {}
选2个 ab   ac     ba   bc      ca   cb       {}
选3个 abc acb     bac  bca     cab  cba      {}

'''
def permutation(self, candidates):
        results = [] #定义结果
        
        #当后续有candidates[i]与candidates[i - 1]的比较时,需要sort
        #candidates.sort()
        
        #DFS的temp都是以空数组/空string开头进行调用的
        #permutation需要visited，以避免重复取
        visited = [False] * len(candidates)
        self.dfs(candidates, visited, [], results) 
        
        return results
        
    #recursion definition     
    def dfs(self, candidates, visited, temp, results): 
        #recursion end case
        #!!!!!!!!!记得写return

        #candidates中的所有值都已经被加入到temp中:
        #return results.append(list(temp))
        if len(temp) == len(candidates):
						results.append(list(temp))
						return

        #recursion explanation
        #镜像对称
        for i in range(len(candidates)): 
						#同start_index一个作用
						if visited[i]:
								continue

            #去重判断(1,2')与(1,2'')
            #if i and nums[i] == nums[i - 1] and not visited[i - 1]:
								#continue
            
            temp.append(candidates[i])#元素写入temp [2]->[2,2]
						visited[i] = True
            self.dfs(candidates, visited, temp, results)
						visited[i] = False
            temp.pop()#弹出元素（因为用过了） [2,2]->[2]
'''
    
Deep Copy:
https://azhang2019.gitbook.io/algorithms/algorithm/di-liu-zhang-yin-shi-tu-shen-du-you-xian-sou-suo/shen-me-shi-deep-copy

1. DFS模板:
    def combination(self, candidates, target):
        results = [] #定义结果
        
        #当后续有candidates[i]与candidates[i - 1]的比较时,需要sort
        #candidates.sort()
        
        #DFS的temp都是以空数组/空string开头进行调用的
        self.dfs(candidates, 0, [], results) 
        #有target时
        self.dfs(candidates, 0, [], results, target) 
        #当要所有candidates的值每次都要被全部放入temp时,需要visited,避免重复取
        #visited = [False] * len(candidates)
        #self.dfs(candidates, visited, [], results, target) 
        
        return results
        
    #recursion definition     
    def dfs(self, candidates, start_index, temp, results, cur_target): 
        #recursion end case
        #!!!!!!!!!记得写return
        if end case条件:
          return results.append(list(temp))
        #target情况
        if cur_target < 0:
            return
        if cur_target == 0: 
            return results.append(list(temp))
        #permutations情况:
        #if len(temp) == len(candidates)

        #recursion explanation
        #镜像对称
        for i in range(start_index, len(candidates)): 
            #去重判断
            #if i > start_index and nums[i] == nums[i - 1]
            #if i and nums[i] == nums[i - 1] and not visited[i - 1]
            
            temp.append(candidates[i])#元素写入temp [2]->[2,2]
            #cur_target -= candidates[i]
            #注意i or i + 1
            self.dfs(candidates, i, temp, results, cur_target) 
            #cur_target += candidates[i]
            temp.pop()#弹出元素（因为用过了） [2,2]->[2]
 
2. 组合的几个关键问题:
2.1 起始索引i在递归函数dfs中怎么变化？ 
i=i，一个元素可以被多次使用 
i=i+1;一个元素只能被用一次 
self.dfs(candidates, i, temp, results, cur_target)
self.dfs(candidates, i + 1, temp, results, cur_target)
2.2 dfs如何移除最后一个元素？ temp.pop()
2.3 假如数组中包含多个相同的元素，但是这些元素每个只能选一次，并且结果中不能出现相同的组合，怎么办？ 
先提前sort好，然后
if i > startIndex and nums[i] == nums[i - 1]:
    continue
 
 
3. combinations要在在1-n的范围内选择k个数时,想明白以下几点： 
3.1 搜索的起始位置是什么（是i还是i++？） 
3.2 搜索的出口是什么？（是否满足了所有的限制条件？target<0和target=0)
3.3 无效的答案是否提前进行了剪枝？
！！！建议在每个确定无效或有效的solution都添加return


******************************************************************************************************************
分析步骤：
1.是不是要将所有的值都排列出来,即permutation problem:用visited
2.每次的取值是不是根据某种规则选取数,即combination problem:用start_index
3.nums是不是存在重复数值([1,2',2'']):yes用nums[i] == nums[i - 1] not visited[i - 1] or i > start_index(##记得sort)
4.combination时,每次的取值是不是能取相同index的值(2+2=4):yes i; no i + 1
******************************************************************************************************************

                 
#注意4和5的区别！！！！                 
4.permutations设置一个visited
[1,2',2'']
visited是用于规定每个存在于nums的值只能被取一次:在为temp加入数据时,2'和2''都能被加到temp中[1,2',2''],但都不能被重复加入[1,2'',2'']or[1,2',2']
当要求nums的每个值都需要加入temp的时候,则需要用一个visited来限制,使得每个值不会被重复放入temp

Combination Sum中同理情况
由于数据选取可以重复,因此在后续dfs调用的时候为i;但Combination Sum II的数据不能重复选取,因此每次dfs时是i+1

                 
5.去重
先提前sort好
[1,2',2'']
#Combination Sum和Combination Sum II
if i > start_index and nums[i] == nums[i - 1]是防止重复情况的出现:[1,2']被分析后,[1,2'']就不用分析了,因为结果是一样的
#Permutations II
if i and nums[i] == nums[i - 1] and not visited[i - 1],即当访问到nums[i] = 2''时,nums[i - 1] = 2'不在temp中,即不是[1,2',2'']情况
