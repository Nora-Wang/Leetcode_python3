Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.


思路:
用hash解决问题,重点是key的选取:用排序后的word作为key,将原始word作为value加入到dict中


code:
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []
        
        dict_strs = {}
        for word in strs:
            word_sorted = self.get_sorted_word(word)
            if word_sorted not in dict_strs:
                dict_strs[word_sorted] = []
            dict_strs[word_sorted].append(word)
            
        result = []
        for word_sorted in dict_strs:
            result.append(dict_strs[word_sorted])
            
        return result
    
    def get_sorted_word(self, word):
        #注意sorted函数的结果是一个list
        return str(sorted(word))
        
        
