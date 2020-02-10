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
        
        hash_record = collections.defaultdict(list)
        
        for word in strs:
            hash_record[str(sorted(word))].append(word)
        
        result = []
        for word in hash_record:
            result.append(hash_record[word])
        
        return result
        
        
