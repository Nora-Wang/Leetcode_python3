Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.


# 方法1
'''
brute force
1. choose shortest word
2. compare shortest word's each prefix with other words's prefix to find the longest prefix
        
time: O(shortest_word_length * number_of_other_words * shortest_word_length)
          第一层for循环           第二层for循环              if语句比较(worse case就是将整个shortest_word都比较一遍)
space: O(shortest_word_length): 有一个shortes_word
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge case
        if not strs:
            return ''
        
        # step 1
        shortes_word = strs[0]
        for word in strs:
            if len(word) < len(shortes_word):
                shortes_word = word
        
        # step 2
        longest_length = 0
        
        for i in range(1, len(shortes_word) + 1):
            # varify whether all the other words have the same prefix shortes_word[:i]
            count = 0
            for other_word in strs:
                if shortes_word[:i] == other_word[:i]:
                    count += 1
            
            # if all the other words have the same prefix shortes_word[:i] -> renew longest_length
            if count == len(strs):
                longest_length = i
        
        return shortes_word[:longest_length]


# optimization
# 在两层for循环中的if比较可以用更省时间的方法进行优化: 每一次其实只用比较当前char就可以了。
# 如果当前char不相等，则说明当前prefix shortes_word[:i + 1]不是存在于strs的每个words里，则直接返回上一个prefix  shortes_word[:i]即可，因为后面的prefix肯定都不符合要求
# time: O(shortest_word_length * number_of_other_words)
          第一层for循环           第二层for循环    
# space: O(shortest_word_length): 有一个shortes_word
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        shortes_word = strs[0]
        for word in strs:
            if len(word) < len(shortes_word):
                shortes_word = word
        
        longest_length = 0
        
        for i in range(len(shortes_word)):
            for other_word in strs:
                if shortes_word[i] != other_word[i]:
                    return shortes_word[:i]
        
        return shortes_word
