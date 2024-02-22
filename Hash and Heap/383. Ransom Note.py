Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.


# HashMap
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        count_r = collections.Counter(ransomNote)
        count_m = collections.Counter(magazine)
        
        for char,count in count_r.items():
            if char not in count_m or count_m[char] < count_r[char]:
                return False
        
        return True

  # List
  class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26
        
        index_a = ord('a')
        for char in ransomNote:
            record[ord(char) - index_a] += 1
        
        for char in magazine:
            record[ord(char) - index_a] -= 1
        
        for num in record:
            if num > 0:
                return False
        
        return True
