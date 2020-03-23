Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.



建一个hashmap来存对应关系，key = pattern, value = str, a->dog, b->cat，循环一遍如果一样就return true，有不一样return false
注意题目中用hash_record.values()来避免ab = “cat cat”这种情况,有的话return false

#3/23/2020
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        record = {}
        str_list = str.split()
        
        #corner case
        if len(pattern) != len(str_list):
            return False
        
        for i in range(len(pattern)):
            #当不在hash表中时
            if pattern[i] in record:
                #pattern = "aaaa", str = "dog cat cat dog"
                if record[pattern[i]] != str_list[i]:
                    return False
            #当在hash表中时
            else:
                #pattern = "abba", str = "dog dog dog dog"
                if str_list[i] in record.values():
                    return False
            
                record[pattern[i]] = str_list[i]
        
        return True
                

#3/23/2020 用两个hash表来存储
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str_list = str.split()
        
        if len(str_list) != len(pattern):
            return False
        
        p_record = {}
        s_record = {}
        for i in range(len(pattern)):
            if pattern[i] not in p_record and str_list[i] not in s_record:
                p_record[pattern[i]] = str_list[i]
                s_record[str_list[i]] = pattern[i]
                continue
            
            if pattern[i] in p_record and p_record[pattern[i]] != str_list[i]:
                return False
        
            if str_list[i] in s_record and s_record[str_list[i]] != pattern[i]:
                return False
            
        return True
                




code:
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        #将str以空格为标志,分隔
        list_str = str.split(' ')
        
        #当长度不等时,直接返回False
        if len(pattern) != len(list_str):
            return False
        
        #用hashmap存对应关系，key = pattern, value = str
        hash_record = {}
        
        for i in range(len(pattern)):
            #hash_record中当pattern[i]是新的时,list_str[i]也必须是新的
            if pattern[i] not in hash_record:
            
                #利用dict.values()函数判断dict里是否存在某个value值
                if list_str[i] in hash_record.values():
                    return False
 
                else:
                    hash_record[pattern[i]] = list_str[i]
                    continue
            
            #hash_record中当pattern[i]不是新的时,list_str[i]一定要与之前存入hash_record的值匹配
            else:
                if hash_record[pattern[i]] != list_str[i]:
                    return False
            
        return True
                
            
        
