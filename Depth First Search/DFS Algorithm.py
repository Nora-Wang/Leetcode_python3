BFS时间复杂度取决于同时queue中存在的node的个数n T(n) = O(2^n)
DFS时间复杂度取决于深度,空间复杂度低

找所有具体方案用DFS:除了二叉树以外的 90% DFS的题，要么是排列，要么是组合
找到图中的所有满足条件的路径
路径 = 方案 = 图中节点的排列组合 
很多题不像二叉树那样直接给你一个图(二叉树也是一个图) 
点、边、路径是需要你自己去分析的

eg:
1. Subsets
点:集合中的元素
边:元素与元素之间用有向边连接，小的点指向大的点(为了避免选出 12 和 21 这种重复集合) 
路径:= 子集 = 图中任意点出发到任意点结束的一条路径
2. Permutations
点:每个数为一个点
边:任意两两点之间都有连边，且为无向边
路径:= 排列 = 从任意点出发到任意点结束经过每个点一次且仅一次的路径




1. DFS模板:
    def comnination(self, candidates, target):
        results = [] #定义结果
        
        #当后续有candidates[i]与candidates[i - 1]的比较时,需要sort
        #candidates.sort()
        
        self.dfs(candidates, 0, temp, results) 
        #有target时
        self.dfs(candidates, 0, temp, results, target) 
        #当要所有candidates的值每次都要被全部放入temp时,需要visited,避免重复取
        #visited = [False] * len(candidates)
        #self.dfs(candidates, visited, temp, results, target) 
        
        return results
        
    #recursion definition     
    def dfs(self, candidates, start_index, temp, results, cur_target): 
        #recursion end case
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
            
            temp.append(candidates[i])#元素写入temp 
            #cur_target -= candidates[i]
            #注意i or i + 1
            self.dfs(candidates, i, temp, results, cur_target) 
            #cur_target += candidates[i]
            temp.pop()#弹出元素（因为用过了） 
 
2. 组合的几个关键问题:
2.1 起始索引i在递归函数dfs中怎么变化？ 
i=i，一个元素可以被多次使用 
i=i+1;一个元素只能被用一次 
self.dfs(candidates, i, temp, results, cur_target)
self.dfs(candidates, i + 1, temp, results, cur_target)
2.2 dfs如何移除最后一个元素？ temp.pop()
2.3 假如数组中包含多个相同的元素，但是这些元素每个只能选一次，并且结果中不能出现相同的组合，怎么办？ 
if i > startIndex and nums[i] == nums[i - 1]:
    continue
 
 
3. combinations要在在1-n的范围内选择k个数时,想明白以下几点： 
3.1 搜索的起始位置是什么（是i还是i++？） 
3.2 搜索的出口是什么？（是否满足了所有的限制条件？target<0和target=0)
3.3 无效的答案是否提前进行了剪枝？(建议在每个确定无效或有效的solution都添加return)


注意4和5的区别！！！！
4.permutations设置一个visited
[1,2',2'']
visited的作用是规定每个存在于nums的值只能被取一次:在为temp加入数据时,2'和2''都能被加到temp中[1,2',2''],但都不能被重复加入[1,2'',2'']or[1,2',2']
当要求nums的每个值都需要加入temp的时候,则需要用一个visited来限制,使得每个值不会被重复放入temp

Combination Sum中同理情况
由于数据选取可以重复,因此在后续dfs调用的时候为i;但Combination Sum II的数据不能重复选取,因此每次dfs时是i+1

5.去重
[1,2',2'']
#Combination Sum和Combination Sum II
if i > start_index and nums[i] == nums[i - 1]是防止重复情况的出现:[1,2']被分析后,[1,2'']就不用分析了,因为结果是一样的
#Permutations II
if i and nums[i] == nums[i - 1] and not visited[i - 1],即当访问到nums[i] = 2''时,nums[i - 1] = 2'不在temp中,即不是[1,2',2'']情况
