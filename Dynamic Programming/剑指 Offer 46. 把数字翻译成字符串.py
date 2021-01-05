给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

提示：

0 <= num < 231

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# DP
'''
str(num)
dp[i]: how many results for num[i]
if 0 <= int(num[i - 1:i + 1]) <= 25: dp[i] += dp[i - 2]
dp[i] += dp[i - 1]

dp[0] = 1
dp[1] = 1 if num[:2] > 25 else 2
'''
class Solution:
    def translateNum(self, num: int) -> int:
        if num < 10:
            return 1

        num = str(num)
        dp = [0] * len(num)
        dp[0] = 1
        dp[1] = 1 if int(num[:2]) > 25 else 2

        for i in range(2, len(num)):
            if 10 <= int(num[i - 1:i+1]) <= 25:
                dp[i] += dp[i - 2]
            dp[i] += dp[i - 1]
        
        return dp[-1]
