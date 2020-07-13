Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".


用curt_num记录当前需要repeat多少次，用curt_str记录当前的sub_str，利用stack的先进后出来处理当前square brackets的东西

四种情况
1）是左括号：将当前的curt_num加入stack，记做后续sub_str需要repeat的count数；将当前curt_str加入stack，记做prev_str；将curt_num, curt_str都归零（另起一循环了）
2）是右括号：意味着当前循环结束，将prev_str给pop出，再将curt_str需要repeat多少次的count pop出，两者结合后再赋值给curt_str
3）是数字：就累加之前有的数字
4）是普通字母：直接加到curt_str里

#time: O(n), space: O(n)
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ''
        
        curt_num = 0
        curt_str = []
        stack = []
        
        for c in s:
            if c == '[':
                stack.append(curt_str)
                stack.append(curt_num)
                curt_str = []
                curt_num = 0
            elif c == ']':
                repeat = stack.pop()
                prev_str = stack.pop()
                for _ in range(repeat):
                    prev_str.extend(curt_str)
                curt_str = prev_str
            elif c.isdigit():
                curt_num = curt_num * 10 + int(c)
            else:
                curt_str.append(c)
        
        return ''.join(curt_str)


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
