Prime factorize a given integer.

Example
Example 1:

Input: 10
Output: [2, 5]
Example 2:

Input: 660
Output: [2, 2, 3, 5, 11]
Notice
You should sort the factors in ascending order.


具体步骤
1.记up=根号n,作为质因数k的上界, 初始化k=2。
2.k<=up且n不为1时，执行步骤3，否则执行步骤4。
3.当n被k整除时，不断整除并覆盖n，同时结果中记录k，直到n不能整出k为止。之后k自增，执行步骤2。
4.当n不为1时，把n也加入结果当中，算法结束。

几点解释
1.不需要判定k是否为质数，如果k不为质数，且能整除n时，n早被k的因数所除。故能整除n的k必是质数。（即在除以6之前，已经被2和3 factorize了）
2.为何引入up？为了优化性能。当k大于up时，k已不可能整除n，除非k是n自身。也即为何步骤4判断n是否为1，n不为1时必是比up大的质数。
3.步骤2中，也判定n是否为1，这也是为了性能，当n已为1时，可早停。


时间复杂度：最坏n为质数时，O(根号n)

code:
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        up = int(math.sqrt(num))
        k = 2
        result = []
        
        while k <= up and num > 1:
            while num % k == 0:
                num //= k
                result.append(k)
            k += 1
        if num > 1:
            result.append(num)
        return result
