You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.



# Set allowed + for loop for each char in word
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(list(allowed))
        
        result = 0
        for word in words:
            is_consistent = True
            for char in word:
                if char not in allowed_set:
                    is_consistent = False
                    break
            
            result += 1 if is_consistent else 0
        
        return result

# Set both allowed and word + for loop char
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(list(allowed))
        
        result = 0
        for word in words:
            word_set = set(list(word))
            
            is_consistent = True
            for char in word_set:
                if char not in allowed_set:
                    is_consistent = False
                    break
            
            if is_consistent:
                result += 1
        
        return result

# Set b.issubset(a)
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(list(allowed))
        
        result = 0
        for word in words:
            word_set = set(list(word))
            
            if word_set.issubset(allowed_set):
                result += 1
        
        return result

# Bit
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_record = [0] * 26
        char_a = ord('a')
        for char in allowed:
            allowed_record[ord(char) - char_a] = 1
        
        result = 0
        for word in words:
            is_consistent = True
            for char in word:
                if not allowed_record[ord(char) - char_a]:
                    is_consistent = False
                    break
            
            if is_consistent:
                result += 1
        
        return result
