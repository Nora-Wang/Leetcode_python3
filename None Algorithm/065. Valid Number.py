Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.


# 10/09/2020
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False
        
        has_num = False
        has_e = False
        has_point = False
        
        s = s.strip()
        
        for i,c in enumerate(s):
            if '0' <= c <= '9':
                has_num = True
                
            elif c == 'e':
                if has_e or not has_num or i == len(s) - 1:
                    return False
                has_e = True
                has_num = False
            
            elif c == '+' or c == '-':
                if i != 0 and ((not has_e) or s[i - 1] != 'e'):
                    return False
                
            elif c == '.':
                if has_point or has_e:
                    return False
                has_point = True
            
            else:
                return False
                
        return has_num
                
            









思路:
一个数怎么构成: 符号+浮点数+'e'+符号+整数

code:
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        s = s.strip() + ' '
        length = len(s) - 1
        
        #开头的符号+/-
        if s[i] == '+' or s[i] == '-':
            i += 1
            
        #开头的符号后面可直接跟e,也可以跟浮点数/整数再跟e
        #count数字和浮点的个数,用浮点数的标准判断(只能有一个'.',且至少有一个数字),这样整数也可直接一起判断
        is_digit, is_point = 0, 0
        while s[i].isdigit() or s[i] == '.':
            if s[i].isdigit():
                is_digit += 1
            else:
                is_point += 1
            i += 1
        if is_digit < 1 or is_point > 1:
            return False
        
        #有e的情况:e的后面一定有整数,且整数可带符号
        if s[i] == 'e':
            i += 1
            if s[i] == '+' or s[i] == '-':
                i += 1
#e后面必须带一个整数
            if i == length:
                return False
            while s[i].isdigit():
                i += 1
                
        #防止中间部分出现其他符号的情况
        return i == length
