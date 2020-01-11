Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.


code:
#用heap,import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        
        heap = [1]
        visited = set([1])
        
        for _ in range(n):
            ugly_num = heapq.heappop(heap)
            
            for positive_num in [2,3,5]:
                new_ugly = ugly_num * positive_num
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        return ugly_num
        
        
        
#brute force
#思路就是用record来记录出现过的ugly number
#这里之所以要用list,是因为在每次计算r2/r3/r5时不知道是在哪一个数的基础上乘以2/3/5,因此这里利用list的index来记录当前*2/3/5后的数,取最小值,
#当数据被取后再用index+1的方式计算下一个数*2/3/5的结果,继续比较大小
Version 1 better
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        
        record = [1]
        p2, p3, p5 = 0, 0, 0
        
        while len(record) < n:
            r2 = record[p2] * 2
            r3 = record[p3] * 3
            r5 = record[p5] * 5
            
            rmin = min(r2, r3, r5)
            
            #这里的重点就是每一次的判断都直接用if即可
            #因为这样可以避免放入record里的数据发生重复
            #eg:在[1,2,3,4,5]后,会发生(p3=1,r3=2*3=6)和(p2=2,r2=3*2=6)的情况,这时rmin=6,用两个if可使p2和p3同时+1,以此避免6重复出现的情况
            if rmin == r2:
                p2 += 1
            if rmin == r3:
                p3 += 1
            if rmin == r5:
                p5 += 1
            
            record.append(rmin)
        
        return record[-1]
            
            

Version 2
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        
        record = [1]
        p2, p3, p5 = 0, 0, 0
        
        while len(record) < n:
            r2 = record[p2] * 2
            r3 = record[p3] * 3
            r5 = record[p5] * 5
            
            rmin = min(r2, r3, r5)
            
            #这里用elif的条件就会出现当6出现后,只有p2+1,而此时r3得到的结果依然是6
            #因此需要在后面加一个if判断,在下一次循环时r2=8,r3=6,r5=10,得到r3最小,让p3+1,
            #然后用if语句发现r3与当前record中的最大值相等,为避免重复当前r则不再放入record中
            if rmin == r2:
                p2 += 1
            elif rmin == r3:
                p3 += 1
            elif rmin == r5:
                p5 += 1
                
            if rmin == record[-1]:
                continue
            
            record.append(rmin)
        
        return record[-1]
            
            
        
