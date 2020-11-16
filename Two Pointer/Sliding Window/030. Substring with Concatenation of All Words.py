You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

 

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
 

Constraints:

1 <= s.length <= 104
s consists of lower-case English letters.
1 <= words.length <= 5000
1 <= words[i].length <= 30
words[i] consists of lower-case English letters.


# 与76题很像，但这里的words是一个个单词，有一定的长度 -> 不可避免的需要第二层循环
# time: O(w) + O(s - w') * O(w) = O(s- w) * O(w), space: O(w)
# w = len(words), w' = total length of the words = w * length_of_each_word, s = len(s)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        # hash_w = {word:freq}
        hash_w = collections.Counter(words)
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        
        if total_len > len(s):
            return []
        
        res = []
            
        for i in range(len(s) - total_len + 1):
            # hash_s = {word:freq} in s[i:i+total_len]
            hash_s = collections.defaultdict(int)
            # how many words in words are also in s[i:i+total_len]
            match = 0
            
            for j in range(i, i + total_len, word_len):
                curt_word = s[j:j+word_len]
                if curt_word in hash_w:
                    hash_s[curt_word] += 1
                    if hash_s[curt_word] == hash_w[curt_word]:
                        match += 1
                    # if curt_word_freq > hash_w -> curt substring s[i:i+total_len] cannot includes all words
                    if hash_s[curt_word] > hash_w[curt_word]:
                        break
                else:
                    break
            
            if match == len(hash_w):
                res.append(i)
        
        return res
            
        
        
        
        
        
