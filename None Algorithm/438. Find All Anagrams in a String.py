Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

这题的考点 sliding window + hash
这道题的最优解是 sliding window + abs_sum_count



基本的想法:假设p串的长度为l,s串长度为n,那么就枚举出s中所有长度为l的子串，并用hash统计它们元素出现的个数
基本想法的时间复杂度:n个子串,每次统计子串中元素出现的个数O(l),每次和p对比元素出现次数是否一样O(256)/O(1),总体O( n * (l + 256/1)) = O(n * l)
#######这样会超时
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        
        result = []
        for i in range(len(s) - len(p) + 1):
            if self.is_anagrams(s[i:i + len(p)], p):
                result.append(i)
                
        return result
    
    def is_anagrams(self, new_s, p):
        if new_s == p:
            return True
        
        count_s, count_p = {}, {}
        
        for i in range(len(p)):
            if new_s[i] not in count_s:
                count_s[new_s[i]] = 0
            count_s[new_s[i]] += 1
            
            if p[i] not in count_p:
                count_p[p[i]] = 0
            count_p[p[i]] += 1
            
        return count_s == count_p
  


Solution:九章高频班给出使用sliding window,避免重复生成count_s
    
Version 1:还是使用hash，但count_p和count_s只是一开始的时候一次建立,后面使用sliding window
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #corner case
        if len(s) < len(p):
            return []
        
        if s == p:
            return [0]
        
        #生成count_p和count_s
        count_p = {}
        count_s = {}
        for i in range(len(p)):
            if p[i] not in count_p:
                count_p[p[i]] = 0
            count_p[p[i]] += 1
            
            if s[i] not in count_s:
                count_s[s[i]] = 0
            count_s[s[i]] += 1
            
        #判断0是否成立
        result = []
        if count_s == count_p:
            result.append(0)
        
        #sliding window:将s[i]删除,并将s[i + len(p)]添加进count
        for i in range(len(s) - len(p)):
            count_s[s[i]] -= 1
            #注意,这里因为是比较的hash,若count_s[s[i]]为0了一定要删除,否则无法==count_p
            #eg:eabc, abc中,若当e不在s[i:i+len(p)]中了,就需要将e从count_s中删除,否则count_s中始终有一个key=e,则无法满足count_s==count_p
            if count_s[s[i]] == 0:
                del count_s[s[i]]
                
            #eg:eabc, abc中,一开始c并不在count_s中,因此需要额外加入  
            if s[i + len(p)] not in count_s:
                count_s[s[i + len(p)]] = 0
            count_s[s[i + len(p)]] += 1
            
            #注意这里是i+1,举个例子就懂了
            #由于每次比较的是count的每个值,因此时间复杂度为O(l)
            if count_s == count_p:
                result.append(i + 1)
        
        return result
        
时间复杂度:若len(s) = n, len(p) = l
T(n) = O(l+l+(n-l)*l)
l大时,O(n*l)
l小时,O(n)
        
            
Version 2: 用list做,并且使用 - ord('a')以减小list的长度
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        if s == p:
            return [0]
        
        #初始化count
        count = [0] * 26
        for i in range(len(p)):
            count[ord(p[i]) - ord('a')] -= 1
            count[ord(s[i]) - ord('a')] += 1

        result = []
        #0的情况
        if self.is_anagram(count):
            result.append(0)
            
        #sliding window:将s[i]对应的count-1,并将s[i + len(p)]对应的count+1
        #注意这里就不用当count为0时,将key删除,因为这里相当于是将26个字母都存进去了,每次直接+/-1,然后判断是否全为0即可
        for i in range(len(s) - len(p)):
            count[ord(s[i]) - ord('a')] -= 1
            count[ord(s[i + len(p)]) - ord('a')] += 1
            
            #由于每次比较的是count的每个值,因此时间复杂度为O(l)
            if self.is_anagram(count):
                result.append(i + 1)
        
        return result
    
    def is_anagram(self, count):
        for i in count:
            if i != 0:
                return False
        return True
            

Version 3:九章高频班进阶版,只使用一个list,并且使用abs_sum_count存储count中的值,避免每次使用O(l)的时间判断count是否全为0
(这里还是用了-97,即- ord('a'),这样可以使得list从256变为26,因为题中说了只有小写字母)
**************时间复杂度为T(n) = O(l + 26 + n - l) = O(n)
 class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        if s == p:
            return [0]
        
        #初始化count
        count = [0] * 26
        for i in range(len(p)):
            count[ord(p[i]) - 97] -= 1
            count[ord(s[i]) - 97] += 1
        
        result = []
        #初始化abs_sum_count
        abs_sum_count = 0
        for item in count:
            abs_sum_count += abs(item)
        #分析0的情况
        if abs_sum_count == 0:
            result.append(0)
        
        #具体思路:每次先把s[i]和s[i + len(p)]对应的count的值减了,将s[i]和s[i + len(p)]的count值+1,-1的变好后,再重新加入abs_sum_count
        #为什么一定要先把全部的值给减了,变好后再加上去？
        #因为每次计算abs_sum_count时,要取的值是s[i]和s[i + len(p)]对应count的绝对值,不好直接加减,只能先减,等变成最新的值后直接去绝对值再加回去
        for i in range(len(s) - len(p)):
            abs_sum_count = abs_sum_count - abs(count[ord(s[i]) - 97]) - abs(count[ord(s[i + len(p)]) - 97])
            count[ord(s[i]) - 97] -= 1
            count[ord(s[i + len(p)]) - 97] += 1
            abs_sum_count = abs_sum_count + abs(count[ord(s[i]) - 97]) + abs(count[ord(s[i + len(p)]) - 97])
            
            #由于比较的不是count的每个值了,因此此处时间复杂度为O(1)
            if abs_sum_count == 0:
                result.append(i + 1)
        
        return result
            
            
            
                   
        
