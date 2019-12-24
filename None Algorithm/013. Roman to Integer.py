Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.




code:
Version 1:将1/4/5/9的特例都写出来,若是特例,则i+2;若不是,则i+1
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
                  'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
                  'C': 100, 'CD': 400, 'D': 500, 'CM': 900,
                  'M': 1000}
        
        i = 0
        result = 0
        while i < len(s):
            if s[i:i+2] in mapping:
                result += mapping[s[i:i+2]]
                i += 2
            else:
                result += mapping[s[i]]
                i += 1
        
        return result
        

Version 2:不写4/9特例,当后一个的值比前一个大时,则用后一个减去前一个即可
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        i = 0
        result = 0
        while i < len(s):
            #注意需要特判i+1,这里容易out of index
            if i + 1 < len(s) and mapping[s[i]] < mapping[s[i + 1]]:
                result += mapping[s[i + 1]] - mapping[s[i]]
                i += 2
            else:
                result += mapping[s[i]]
                i += 1
        
        return result

#Version 2改编版:防止i out of index,直接只while到len - 1;如果是特例就减，不然加
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        i = 0
        result = 0
        while i < len(s) - 1:
            if mapping[s[i]] < mapping[s[i + 1]]:
                result -= mapping[s[i]]
            else:
                result += mapping[s[i]]
            i += 1
            
        return result + mapping[s[-1]]
