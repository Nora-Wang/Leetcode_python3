Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.



# 10/28/2020
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge case
        if not s or not t or len(s) < len(t):
            return ''
        
        hash_t = collections.Counter(t) # count char freq in t
        hash_s = collections.defaultdict(int) # record char freq in s
        res = ''
        min_length = float('inf')
        match = len(hash_t) # all char in t are in curt_s_window
        right = 0
        
        for left in range(len(s)):
            # create the match window
            while right < len(s) and match != 0:
                if s[right] in hash_t:
                    hash_s[s[right]] += 1
                    if hash_s[s[right]] == hash_t[s[right]]:
                        match -= 1
                        
                right += 1
            
            # renew res and min_length
            if match == 0 and right - left < min_length:
                res = s[left:right]
                min_length = right - left
            
            # move window
            if s[left] not in hash_t:
                continue
            
            if hash_s[s[left]] == hash_t[s[left]]:
                match += 1
            hash_s[s[left]] -= 1
        
        return res




code:
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        result = ''
        #建立目标字符串的哈希表与出现次数，匹配值初始为0
        hash_t = collections.Counter(t)
        hash_s = {}
        j = 0
        count = 0
        min_length = sys.maxsize
        
        for i in range(len(s)):
            #匹配值不足时一直循环
            while j < len(s) and count < len(hash_t):
                #更新窗口哈希
                hash_s[s[j]] = hash_s.get(s[j], 0) + 1
                
                #更新完当前窗口哈希需判断是否达到target要求，如果达到了匹配值加1 
                if s[j] in hash_t and hash_t[s[j]] == hash_s[s[j]]:
                    count += 1
      ！！##一定要记得更新j
                j += 1
                
            #如果长度更短，匹配值正确，更新结果，更新最小长度
            if count == len(hash_t) and j - i < min_length:
                min_length = j - i
                result = s[i:j]
            
            #前指针往后走时需要删除当前s[i],并需要更新当前对应的hash表
            hash_s[s[i]] -= 1
            #当s[i]在target中时,需要判断该次删除是否会影响count
            if s[i] in hash_t and hash_t[s[i]] == hash_s[s[i]] + 1:
                count -= 1
        
        return result
                
