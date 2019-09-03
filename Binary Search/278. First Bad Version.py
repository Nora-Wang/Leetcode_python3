题目：
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

完全的套模板

code:

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n == 0):
            return 1
        start = 1
        end = n
        while start + 1 < end:
            mid = start + (end - start) / 2
            #end和start就直接=mid，别管+1和-1
            if(isBadVersion(mid)):
                end = mid
            else:
                start = mid
        #start和end的顺序要根据情况判断：求最小，先start；求最大，先end。
        #此题因为现在相当于还剩4、5两个version，需要先判断4，若4是false，再判断5是否为true；
        #若先判断5，则4也为true的情况会发生错误
        if(isBadVersion(start)):
            return start
        if(isBadVersion(end)):
            return end
        return 1

