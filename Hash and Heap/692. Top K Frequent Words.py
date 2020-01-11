Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:

Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:

Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:

Try to solve it in O(n log k) time and O(n) extra space.


题目总体思路同347,主要就是sort部分
code:
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        if not words:
            return []
        
        record = {}
        for i in words:
            record[i] = record.get(i, 0) + 1
        
        #sorted的时候先按照出现次数,然后按单词字母顺序排序
        #因此这里的key是-item[1]倒着排序的value值,即按照出现次数由大到小排序;item[0]正着排序的key值,即按照单词word的首字母顺序排序
        sorted_record = sorted(record.items(), key = lambda item:(-item[1], item[0]))
        
        result = []
        for i in range(k):
            result.append(sorted_record[i][0])
        
        return result
