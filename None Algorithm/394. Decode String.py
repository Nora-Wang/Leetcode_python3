Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


四种情况
1）是数字，就累加之前有的数字
2）是左括号，从左括号之后开始递归。递归要传回两个值：组成的substring，递归结束的位置。 之后把传回的substring × 数字 加到结果里。数字归零。
3）是右括号，返回结果
4）是普通字母，直接加到结果里

code:
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''
        
        result, index = self.helper(0, s)
        
        return result
    
    def helper(self, index, s):
        result = ''
        count = 0
        
        while index < len(s):
            if s[index].isdigit():
                count = count * 10 + int(s[index])
            elif s[index] == '[':
                sub_result, index = self.helper(index + 1, s)
                result += sub_result * count
                count = 0
            elif s[index] == ']':
                return result, index
            else:
                result += s[index]
                
            index += 1
        
        return result, index
