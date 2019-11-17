Give a string, you can choose to split the string after one character or two adjacent characters, and make the string to be composed of only one character or two characters. Output all possible results.

Example

Example1

Input: "123"
Output: [["1","2","3"],["12","3"],["1","23"]]
Example2

Input: "12345"
Output: [["1","23","45"],["12","3","45"],["12","34","5"],["1","2","3","45"],["1","2","34","5"],["1","23","4","5"],["12","3","4","5"],["1","2","3","4","5"]]



code:
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        results = []
        self.dfs(s, [], results)
        
        return results
        
    def dfs(self, s, temp, results):
        if s == '':
            results.append(list(temp))
            
        #循环两次,每次取一个值或两个值
        for i in range(2):
            #判断剩下的s长度是否大于i+1,如果大于其长度,证明没有足够的长度可以取
            if i + 1 > len(s):
                continue
            
            #前i位进temp,i+1之后递归
            temp.append(s[:i + 1])
            self.dfs(s[i + 1:], temp, results)
            temp.pop()
