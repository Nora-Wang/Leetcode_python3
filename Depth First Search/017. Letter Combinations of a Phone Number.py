Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.



注意KEYBROAD的写法(dict的写法,注意:,符号)

使用dfs求解，整个递归分为 len(digits) 层，每层考虑一个 input 的数字，每层有当前层数次对应字母个数个分支，
时间复杂度大约为 O(每个数字对应字母个数 ^ len(digits))，空间复杂度如果不考虑解集占用空间，为递归栈所占，O(len(digits))

code:
KEYBROAD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        results = []
        self.dfs(digits, 0, [], results)
        
        return results
    
    def dfs(self, digits, index, temp, results):
        if len(temp) == len(digits):
            results.append(''.join(temp))
            #一定要return,否则后面的KEYBROAD会out of range
            return
            
        #index的作用是取到digits的第几个值
        for letter in KEYBROAD[digits[index]]:
            temp.append(letter)
            self.dfs(digits, index + 1, temp, results)
            temp.pop()
        
