Given a string, find all permutations of it without duplicates.

Example

Example 1:

Input: "abb"
Output:
["abb", "bab", "bba"]
Example 2:

Input: "aabb"
Output:
["aabb", "abab", "baba", "bbaa", "abba", "baab"]


基本和047. Permutations II一样
只是需要处理一下str,将其转换为list
并且在将temp加入results时需要将其转换为str形式(用''.join(temp))


class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        str = sorted(list(str))
        results = []
        visited = [False] * len(str)
        self.dfs(str, [], visited, results)
        
        return results
        
    def dfs(self, str, temp, visited, results):
        
        if len(temp) == len(str):
            results.append(''.join(temp))
            
        for i in range(len(str)):
            if visited[i]:
                continue
            
            if i and str[i] == str[i - 1] and not visited[i - 1]:
                continue
            
            temp.append(str[i])
            visited[i] = True
            self.dfs(str, temp, visited, results)
            visited[i] = False
            temp.pop()
