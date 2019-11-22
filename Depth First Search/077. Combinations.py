Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]




class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if not n or not k:
            return []
            
        results = []
        self.dfs(n, k, 0, [], results)
        
        return results
        
    def dfs(self, n, k, start_value, temp, results):
        if len(temp) == k:
            results.append(list(temp))
            return
        
        for i in range(start_value, n):
            #当剩余的数的个数<还需要append进temp的数的个数时,后续都不用再dfs了
            if n - i + 1 < k - len(temp):
                return
            temp.append(i + 1)
            self.dfs(n, k, i + 1, temp, results)
            temp.pop()
            
