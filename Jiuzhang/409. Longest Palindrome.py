Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.


思路：
题目给了我们一个字符串，让我们找出可以组成的最长的回文串的长度。由于字符顺序可以打乱，所以问题就转化为了求偶数个字符的个数。
我们了解回文串的都知道，回文串主要有两种形式，一个是左右完全对称的，比如noon;还有一种是以中间字符为中心，左右对称，比如bob，level等.
那么我们统计出来所有偶数个字符的出现总和，然后如果有奇数个字符的话，我们取出其最大偶数，然后最后结果加1即可，

具体解法：
先过一遍字符串，用hash存起来每个字母出现的次数，然后在v的个数大于1的情况下，看看这个次数是不是偶数。
如果是就直接加到counter里；如果不是，那就取出其最大偶数，即要减一后加到counter里。
然后一定要判断所有的次数里有没有奇数，有的话最终的结果再加一。（即bool值hashodd的作用）

注意：
hashodd的设置是一个bool值，因为若为奇数，只有一个能被放在中间，其他的最多把偶数个放两边，剩余的单个的都不能用。因此最后的count只用加一就好。

code:
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        dic = {}
        for i in s:
            if i in dic:
                del dic[i]
            else:
                dic[i] = True
                
        remove = len(dic)        
        if remove:
            remove -= 1
            
        return len(s) - remove
        
            
    
    
    
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        for letter in s:
            if letter in hash:
                hash[letter] += 1
            else:
                hash[letter] = 1
        hashodd = False
        count = 0
        for k,v in hash.items():
            if v > 1:
                if v % 2 == 0:
                    count += v
                else:
                    count += v - 1
                    hashodd = True
            else:
                hashodd = True
        if hashodd:
            count += 1
        return count
