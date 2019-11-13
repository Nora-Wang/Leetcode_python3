combination模板：
    def comnination(self, candidates, target):
        self.res = [] #定义结果
        self.dfs(candidates, [], target, 0) 
        return self.res
         
    def dfs(self, candidates, temp, remainder, index): 
        if remainder == 0: 
            self.res.append(temp[:]) #temp写入res,注意temp的写法
            return 

        #循环遍历 
        for i in range(index, len(candidates)): 
            temp.append(candidates[i])#元素写入temp 
            dfs(candidates, temp, remainder - candidates[i], i) 
            temp.pop()#弹出元素（因为用过了） 

     
 
组合的几个关键问题： 
1.起始索引i在递归函数dfs中怎么变化？ 
i=i，一个元素可以被多次使用 
i=i+1;一个元素只能被用一次 
dfs(candidates, temp, remainder - candidates[i], 1+1)

2.dfs如何移除最后一个元素？ 
tmpList.remove(tmpList.size()-1); 

3.假如数组中包含多个相同的元素，但是这些元素每个只能选一次，并且结果中不能出现相同的组合，怎么办？ 
if(i != startIndex && nums[i]==nums[i-1]{ 
continue; 
} 
i index 
continue 
and 
candidates [ i ] 
candidates [i -1] 
 
 
combinations要在在1-n的范围内选择k个数： 
想明白以下几点： 
搜索的起始位置是什么（是1还是0？） 
搜索的终点是什么？（是<=还是<?) 
搜索的出口是什么？（是否满足了所有的限制条件？） 
无效的答案是否提前进行了剪枝？（建议在每个确定无效或有效的solution都添加return） 
 
remove的参数是索引 
