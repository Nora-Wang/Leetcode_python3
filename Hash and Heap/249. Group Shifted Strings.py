Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output: 
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]


code:
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        if not strings:
            return []
        
        hash_record = collections.defaultdict(list)
        
        for word in strings:
            num = self.get_num(word)
            hash_record[num].append(word)
        
        result = []
        for num in hash_record:
            result.append(hash_record[num])
        
        return result
    
    
    def get_num(self, word):
        result = ''
        
        #这里要注意
        #1. az的结果为25,而ab的结果为-1,但两个情况应该是一样的;所以这里用+26,%26得到同样的num
        #2. result的存法是每个值前面加一个空格,因为有case:'abc', num = '12'; 'am', num = '12';
        #但abc的num是b->1,c->2,而am的num是m->12;这样结果都为'12',但意义确是不一样的,因此需要用空格将每个字母得到的num分开
        for i in range(1, len(word)):
            count = ord(word[i]) - ord(word[0]) + 26
            result += ' ' + str(count % 26)
        
        return result
