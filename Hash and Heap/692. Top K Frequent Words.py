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




#1. 直接用hash + sort的方式
#time: O(nlogn), space: O(n)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return []
        
        f_count = collections.Counter(words)
        
        #这个sort是按照frequency的逆序+word的增序排列的
        sorted_w = sorted(f_count.items(), key=lambda x:(-x[1], x[0]))
        
        #一句话代表下面5行代码: return [sorted_w[i][0] for i in range(k if k <= len(sorted_w) else len(sorted_w))]
        res = []
        for i in range(k if k <= len(sorted_w) else len(sorted_w)):
            res.append(sorted_w[i][0])
            
        return res


#2. max heap: heapify all the hash_table, use max-heap to pop the top k one by one (or use nsmallest function.)
#time: O(nlogn), space: O(n)
'''
这里如果用min heap会很麻烦，因为在排序的时候会先将frequency小的pop出去，问题是word order较小的也会被先pop，这与题目意思违背.而想要设置word较大的先被pop会很麻烦.
因此采用frequency为负数 + word的排序方式，这样能保证heap在排序时是按照frequency较高 + word较小来排序的
上面不用nlargest也是同样的道理.largest意味着frequency为正，但同时还要满足word较小的先被pop，不好实现.
'''
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words:
            return []
        
        f_count = collections.Counter(words)
        
        #这里不好直接用heapify,因为heapify的对象必须是array,而items出来的结果为dict_items([('i', 2), ('love', 2), ('leetcode', 1), ('coding', 1)])
        heap = []
        for word, f in f_count.items():
            heapq.heappush(heap, (-f, word))
        
        #一句话代表下面6行代码: return [v[1] for v in heapq.nsmallest(k if k <= len(sorted_w) else len(sorted_w), heap)]
        res = []
        while k and heap:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res








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
