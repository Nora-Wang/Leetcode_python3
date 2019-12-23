Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:

Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:

Given s = "apple", abbr = "a2e":

Return false.


思路:
• 直接模拟
• s = "internationalization"
• t = "i12iz4n“
• 一个串上一个指针i,j
• 麻烦点:逻辑小细节处理cases(怎样读数字、指针具体指向的位置)

这道题不用判断not len(word) or not len(abbr),因为后续都已判断


code:
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
            
                #case 1: s = 'a', abbr = '01'
                if abbr[j] == '0':
                    return False
                    
                #用于记录数字有多长,方便后续取值
                digit_len = 0
                
#大while套一个小while时,小while很容易越界!!而且要注意j < len(abbr)的放置的顺序
                #case 2: 注意别让j超出范围
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                    digit_len += 1
                i += int(abbr[j - digit_len:j])
                
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        #case 3: s = 'aa', abbr = 'a2'
        return i == len(word) and j == len(abbr)
