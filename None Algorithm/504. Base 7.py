Given an integer, return its base 7 string representation.

Example 1:

Input: 100
Output: "202"
Example 2:

Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].


参考13. Integer to Roman
如何将一个数转成k进制? % k / k

eg:
1. 100 / 7 = 14 余 2
2. 14 / 7 = 2 余 0
3. 2 / 7 = 0 余 2
最后的结果是倒着来的‘202’



code:
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        #注意小于0的情况
        if num < 0:
            return '-' + self.convertToBase7(-num)
        #小于7时直接返回即可,注意str
        if num < 7:
            return str(num)
        #否则用recursion(递归)的方式调用自身函数,注意要将取模放在最后且str
        return self.convertToBase7(num / 7) + str(num % 7)
